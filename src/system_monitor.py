import sys
import os
import subprocess
import psutil
import time
import re
from typing import Dict, Any

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from PySide6.QtCore import QObject, Signal, QTimer
from src.database import DatabaseHandler
from src.gpu_monitor import GPUMonitoring
from src.logger_config import get_logger


class SystemMonitor(QObject):
    """Класс для мониторинга системных ресурсов"""
    update_metrics = Signal(dict)
    update_timer = Signal(str)

    def __init__(self, database_handler: DatabaseHandler | None = None):
        super().__init__()
        self.logger = get_logger(self.__class__.__name__)
        self.logger.info("Инициализация SystemMonitor")

        self._init_system_components(database_handler)
        self._init_time_setting()

    def _init_system_components(self, database_handler: DatabaseHandler | None):
        self.database_handler = database_handler or DatabaseHandler()
        self.gpu_monitoring = GPUMonitoring()
        self.monitoring = False

    def _init_time_setting(self):
        self.start_time = None
        self.metrics_timer = QTimer()
        self.metrics_timer.timeout.connect(self._collect_system_metrics)
        self.timer_updater = QTimer()
        self.timer_updater.timeout.connect(self._update_monitoring_time)
        self.time_lapse = 1

    def set_time_lapse(self, time_lapse: int):
        """Установка интервала обновления"""
        self.time_lapse = time_lapse
        if self.monitoring:
            self.metrics_timer.stop()
            self.metrics_timer.start(self.time_lapse * 1000)
        self.logger.info(f"Интервал обновления установлен: {self.time_lapse} сек.")

    def start_monitoring(self):
        """Запуск мониторинга"""
        if not self.monitoring:
            try:
                self.monitoring = True
                self.start_time = time.time()
                self.metrics_timer.start(self.time_lapse * 1000)
                self.timer_updater.start(1000)
                self.logger.info("Мониторинг запущен")
            except Exception as e:
                self.monitoring = False
                self.logger.error(f"Ошибка при запуске мониторинга: {e}")
                self.stop_monitoring()

    def stop_monitoring(self):
        """Остановка мониторинга"""
        if self.monitoring:
            self.monitoring = False
            self.metrics_timer.stop()
            self.timer_updater.stop()
            self.start_time = None
            self.logger.info("Мониторинг остановлен")

    def _update_monitoring_time(self):
        """Обновление времени мониторинга"""
        try:
            if self.start_time:
                elapsed_time = time.time() - self.start_time
                minutes, seconds = divmod(int(elapsed_time), 60)
                time_str = f"{minutes:02d}:{seconds:02d}"
                self.update_timer.emit(time_str)
        except Exception as e:
            self.logger.error(f"Ошибка обновления времени: {e}")

    def get_monitoring_time(self) -> str:
        """Получение текущего времени мониторинга"""
        if self.start_time:
            elapsed_time = time.time() - self.start_time
            minutes, seconds = divmod(int(elapsed_time), 60)
            return f"{minutes:02d}:{seconds:02d}"
        return ""

    def _collect_system_metrics(self) -> None:
        """Сбор метрик системы"""
        try:
            metrics = self._gather_system_metrics()
            self.database_handler.adding_data(metrics)
            self.update_metrics.emit(metrics)

        except Exception as e:
            self.logger.error(f"Ошибка сбора системных метрик: {e}")

    def _gather_system_metrics(self) -> Dict[str, Any]:
        """Детальный сбор системных метрик"""
        try:
            cpu_usage = psutil.cpu_percent()
            ram_free_mb, total_ram_mb = self.get_ram_info()
            disk_free_gb, total_disk_gb = self.get_rom_info()
            gpu_load = self.gpu_monitoring.get_gpu_load()

            if cpu_usage is None or ram_free_mb is None or total_ram_mb is None:
                raise ValueError("Не удалось получить системные метрики")

            elapsed_time = time.time() - self.start_time if self.start_time else 0
            minutes, seconds = divmod(int(elapsed_time), 60)

            return {
                'time_lapse': self.time_lapse,
                'cpu_percent': cpu_usage,
                'gpu_load': gpu_load,
                'ram_total_mb': total_ram_mb,
                'ram_free_mb': ram_free_mb,
                'disk_total_gb': total_disk_gb,
                'disk_free_gb': disk_free_gb,
                'monitoring_time': f"{minutes:02d}:{seconds:02d}"
            }

        except Exception as e:
            self.logger.error(f"Ошибка получения системных метрик: {e}")
            return {}

    def get_ram_info(self) -> tuple[float, float]:
        try:
            ram = psutil.virtual_memory()
            return round(ram.available / (1024 * 1024), 2), round(ram.total / (1024 * 1024), 2)
        except Exception as e:
            self.logger.error(f"Ошибка получения RAM информации: {e}")
            return 0.0, 0.0

    def get_rom_info(self) -> tuple[float, float]:
        total_disk_gb, disk_free_gb = 0.0, 0.0
        try:
            result = subprocess.run(['df'], stdout=subprocess.PIPE, text=True, check=True)
            output = result.stdout
            lines = output.splitlines()

            if len(lines) < 3:
                self.logger.error(f"Нет доступной информации о дисковом пространстве.")
                return total_disk_gb, disk_free_gb

            device_line = next((line for line in lines if line.startswith('/dev/')), None)

            if device_line is None:
                self.logger.error(f"Не найдено устройство, начинающееся с /dev/")
                return total_disk_gb, disk_free_gb

            else:
                clean_line = re.sub(r'\x1b\[[0-9;]*[mG]', '', device_line)
                parts = clean_line.split()
                if len(parts) < 4:
                    self.logger.error(f"Некорректный формат данных: {clean_line}")
                    return total_disk_gb, disk_free_gb

            total_size = parts[1]
            available_size = parts[3]

            total_size_cleaned = total_size.replace("G", "") if "G" in total_size else total_size
            available_size_cleaned = available_size.replace("G", "") if "G" in available_size else available_size

            try:
                total_disk_gb = round(float(total_size_cleaned) / (1024 * 1024), 1)
                disk_free_gb = round(float(available_size_cleaned) / (1024 * 1024), 1)

            except ValueError:
                self.logger.error(f"Не удалось конвертировать значения в тип float")
                return total_disk_gb, disk_free_gb

            return disk_free_gb, total_disk_gb

        except subprocess.CalledProcessError as e:
            self.logger.error(f"Ошибка выполнения команды pydf: {e}")
            return total_disk_gb, disk_free_gb
        except Exception as e:
            self.logger.error(f"Ошибка при получении информации о памяти: {e}")
            return total_disk_gb, disk_free_gb


    def get_process_resources(self, pid: int) -> Dict[str, float]:
        """
        Получение ресурсов (CPU и Memory) для конкретного процесса
        """
        try:
            # Получаем процесс по PID
            process = psutil.Process(pid)

            # Получаем использование CPU
            cpu_percent = process.cpu_percent(interval=0.1)

            # Получаем использование памяти
            memory_percent = process.memory_percent()

            return {
                'cpu_percent': round(cpu_percent, 2),
                'memory_percent': round(memory_percent, 2)
            }

        except psutil.NoSuchProcess:
            self.logger.error(f"Процесс с PID {pid} не найден")
            return {'cpu_percent': 0.0, 'memory_percent': 0.0}

        except Exception as e:
            self.logger.error(f"Ошибка получения ресурсов процесса: {e}")
            return {'cpu_percent': 0.0, 'memory_percent': 0.0}