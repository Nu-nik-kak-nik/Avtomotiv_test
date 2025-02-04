import os
import platform
from typing import Dict
from dataclasses import dataclass
from functools import cached_property


@dataclass
class SystemInfo:
    """
    Класс для сбора и предоставления системной информации.
    """

    @cached_property
    def os_info(self) -> str:
        """
        Получение информации об операционной системе.

        :return: Строка с информацией об ОС
        """
        return platform.system()

    @cached_property
    def hostname(self) -> str:
        """
        Получение имени хоста.

        :return: Имя компьютера
        """
        return platform.node()

    @cached_property
    def desktop_environment(self) -> str:
        """
        Определение окружения рабочего стола.

        :return: Название окружения рабочего стола
        """
        try:
            return os.environ.get('XDG_CURRENT_DESKTOP', 'Undefined')
        except Exception:
            return 'Unknown'

    @cached_property
    def kernel_version(self) -> str:
        """
        Получение версии ядра.

        :return: Версия ядра Linux
        """
        return platform.release()

    @cached_property
    def cpu_info(self) -> str:
        """
        Получение информации о процессоре.

        :return: Модель и количество ядер процессора
        """
        try:
            with open('/proc/cpuinfo', 'r') as f:
                for line in f:
                    if line.startswith('model name'):
                        return line.split(':')[1].strip()
        except FileNotFoundError:
            return platform.processor()

    @cached_property
    def system_architecture(self) -> str:
        """
        Получение архитектуры системы.

        :return: Архитектура процессора
        """
        return platform.machine()

    def collect_system_info(self) -> Dict[str, str]:
        """
        Сбор всей системной информации.

        :return: Словарь с системной информацией
        """
        return {
            'OS': self.os_info,
            'Hostname': self.hostname,
            'Desktop Environment': self.desktop_environment,
            'Kernel': self.kernel_version,
            'CPU': self.cpu_info,
            'Architecture': self.system_architecture
        }

    def display_info(self) -> str:
        """
        Форматированный вывод системной информации.

        :return: Отформатированная строка с системной информацией
        """
        info = self.collect_system_info()
        return '\n'.join([f"{key}: {value}" for key, value in info.items()])


if __name__ == "__main__":
    system_info = SystemInfo()
    print(system_info.display_info())