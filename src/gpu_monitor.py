import sys
import os
import subprocess
import re


project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)


from src.logger_config import get_logger


class GPUMonitoring:

    def __init__(self):
        self.logger = get_logger(self.__class__.__name__)
        self.logger.info("Инициализация GPUMonitoring")
        self.vendor: str | None = None
        self.model: str | None = None
        self._detect_gpu()

    def _detect_gpu(self)  -> None:
        """
        Обнаружение вендора и модели видеокарты
        """
        supported_vendors = ['NVIDIA', 'AMD', 'Intel']

        try:
            lspci_output = subprocess.run(
                ['lspci', '-vnn'],
                capture_output=True,
                text=True,
                check=True
            ).stdout.splitlines()

            gpu_line = next(
                (line for line in lspci_output
                 if 'VGA' in line and any(vendor in line for vendor in supported_vendors)),
                None
            )
            if not gpu_line:
                raise ValueError("GPU не обнаружена")

            self.vendor: str | None = next(
                (vendor for vendor in supported_vendors if vendor in gpu_line),
                None
            )
            if not self.vendor:
                raise ValueError(f"Неизвестный вендор GPU в строке: {gpu_line}")

            model_match = re.search(r'[\[\(](.*?)[\]\)]', gpu_line)
            self.model: str | None = model_match.group(1) if model_match else None

            self.logger.info(
                "Обнаружена GPU: Вендор = %s, Модель = %s",
                self.vendor,
                self.model or "Неизвестно"
            )

        except subprocess.CalledProcessError as e:
            self.logger.error(
                "Ошибка выполнения команды lspci: код = %d, вывод = %s",
                e.returncode,
                e.output
            )
            raise

        except ValueError as e:
            self.logger.error(str(e))
            raise

        except Exception as e:
            self.logger.error(
                "Неожиданная ошибка при обнаружении GPU: %s",
                str(e),
                exc_info=True
            )
            raise

    def get_gpu_load(self) -> float:
        """
        Получение процента загрузки GPU в зависимости от вендора
        """
        if not self.vendor:
            self.logger.error("GPU не инициализирована")
            return 0.0

        vendors_mapping = {
            'NVIDIA': self.get_nvidia_load,
            'AMD': self.get_amd_load,
            'Intel': self.get_intel_load
        }

        try:
            return vendors_mapping[self.vendor]()

        except Exception as e:
            self.logger.error(f"Ошибка получения загрузки GPU {self.vendor}: {e}")
            return 0.0

        except KeyError:
            self.logger.error(f"Неподдерживаемый вендор GPU: {self.vendor}")
            return 0.0

    def get_nvidia_load(self) -> float:
        try:
            result = subprocess.run(
                ['nvidia-smi', '--query-gpu=utilization.gpu', '--format=csv,noheader,nounits'],
                capture_output=True,
                text=True
            )
            return float(result.stdout.strip())

        except subprocess.CalledProcessError:
            self.logger.error("Ошибка выполнения nvidia-smi")
            return 0.0

        except subprocess.TimeoutExpired:
            self.logger.error("Превышено время ожидания nvidia-smi")
            return 0.0

        except (ValueError, TypeError):
            self.logger.error("Невозможно преобразовать загрузку NVIDIA GPU")
            return 0.0

        except Exception as e:
            self.logger.error(f"Неожиданная ошибка при получении загрузки NVIDIA GPU: {e}")
            return 0.0

    def get_amd_load(self) -> float:
        try:
            with open('/sys/class/drm/renderD128/device/gpu_busy_percent', 'r') as f:
                return float(f.read().strip())

        except FileNotFoundError:
            self.logger.error("Файл gpu_busy_percent для AMD GPU не найден")
            return 0.0

        except (ValueError, TypeError):
            self.logger.error("Невозможно преобразовать загрузку AMD GPU")
            return 0.0

        except Exception as e:
            self.logger.error(f"Неожиданная ошибка при получении загрузки AMD GPU: {e}")
            return 0.0

    def get_intel_load(self) -> float:
        try:
            with open('/sys/class/drm/renderD128/device/gt_cur_freq_mhz', 'r') as f:
                return float(f.read().strip()) / 100

        except FileNotFoundError:
            self.logger.error("Файл gt_cur_freq_mhz для Intel GPU не найден")
            return 0.0

        except (ValueError, TypeError):
            self.logger.error("Невозможно преобразовать загрузку Intel GPU")
            return 0.0

        except Exception as e:
            self.logger.error(f"Неожиданная ошибка при получении загрузки Intel GPU: {e}")
            return 0.0