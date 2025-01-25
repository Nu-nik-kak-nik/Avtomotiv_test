import pytest
import time
import subprocess
import logging
from unittest.mock import patch, MagicMock
from PySide6.QtCore import QTimer

from src.system_monitor import SystemMonitor
from src.database import DatabaseHandler


class TestSystemMonitor:
    @pytest.fixture
    def mock_database_handler(self):
        return MagicMock(spec=DatabaseHandler)

    @pytest.fixture
    def system_monitor(self, mock_database_handler):
        return SystemMonitor(database_handler=mock_database_handler)

    def test_init(self, system_monitor, mock_database_handler):
        assert system_monitor.database_handler == mock_database_handler
        assert system_monitor.monitoring == False
        assert system_monitor.start_time is None
        assert system_monitor.time_lapse == 1
        assert isinstance(system_monitor.metrics_timer, QTimer)
        assert isinstance(system_monitor.timer_updater, QTimer)

    def test_set_time_lapse(self, system_monitor):
        with patch.object(system_monitor.metrics_timer, 'start') as mock_start:
            system_monitor.monitoring = True
            system_monitor.set_time_lapse(5)

            assert system_monitor.time_lapse == 5
            mock_start.assert_called_once_with(5 * 1000)

    def test_start_monitoring(self, system_monitor):
        with patch.object(system_monitor.metrics_timer, 'start'), \
                patch.object(system_monitor.timer_updater, 'start'):
            system_monitor.start_monitoring()

            assert system_monitor.monitoring == True
            assert system_monitor.start_time is not None

    def test_stop_monitoring(self, system_monitor):
        with patch.object(system_monitor.metrics_timer, 'stop'), \
                patch.object(system_monitor.timer_updater, 'stop'):
            system_monitor.monitoring = True
            system_monitor.start_time = time.time()
            system_monitor.stop_monitoring()

            assert system_monitor.monitoring == False
            assert system_monitor.start_time is None

    def test_get_monitoring_time(self, system_monitor):
        system_monitor.start_time = time.time() - 125
        assert system_monitor.get_monitoring_time() == "02:05"
        system_monitor.start_time = None
        assert system_monitor.get_monitoring_time() == ""

    @patch('psutil.cpu_percent')
    @patch('psutil.virtual_memory')
    def test_get_ram_info(self, mock_virtual_memory, mock_cpu_percent, system_monitor):
        mock_memory = MagicMock()
        mock_memory.available = 4 * 1024 * 1024
        mock_memory.total = 8 * 1024 * 1024
        mock_virtual_memory.return_value = mock_memory
        free_ram, total_ram = system_monitor.get_ram_info()

        assert free_ram == 4.0
        assert total_ram == 8.0

    def test_gather_system_metrics(self, system_monitor):
        with patch.object(system_monitor, 'get_ram_info', return_value=(4000.0, 8000.0)), \
                patch.object(system_monitor, 'get_rom_info', return_value=(50.0, 100.0)), \
                patch('psutil.cpu_percent', return_value=50.0):
            system_monitor.start_time = time.time() - 125  # 2 минуты 5 секунд
            metrics = system_monitor._gather_system_metrics()
            assert metrics['cpu_percent'] == 50.0
            assert metrics['ram_free_mb'] == 4000.0
            assert metrics['ram_total_mb'] == 8000.0
            assert metrics['disk_free_gb'] == 50.0
            assert metrics['disk_total_gb'] == 100.0
            assert metrics['monitoring_time'] == "02:05"

    def test_collect_system_metrics(self, system_monitor, mock_database_handler):
        with patch.object(system_monitor, '_gather_system_metrics', return_value={'cpu': 50}):
            system_monitor._collect_system_metrics()
            mock_database_handler.adding_data.assert_called_once_with({'cpu': 50})

    def test_start_monitoring_exception(self, system_monitor):
        with patch.object(system_monitor.metrics_timer, 'start', side_effect=Exception("Test error")), \
                patch.object(system_monitor, 'stop_monitoring') as mock_stop:
            system_monitor.monitoring = False
            system_monitor.start_monitoring()
            assert system_monitor.monitoring == False
            mock_stop.assert_called_once()

    def test_update_monitoring_time(self, system_monitor):
        mock_signal = MagicMock()
        system_monitor.update_timer = mock_signal
        system_monitor.start_time = time.time() - 125
        system_monitor._update_monitoring_time()
        mock_signal.emit.assert_called_once_with("02:05")

    def test_update_monitoring_time_no_start_time(self, system_monitor):
        system_monitor.start_time = None
        with patch.object(system_monitor, '_update_monitoring_time') as mock_method:
            system_monitor._update_monitoring_time()
            mock_method.assert_called_once()

    def test_get_rom_info_subprocess_error(self, system_monitor):
        with patch('subprocess.run', side_effect=subprocess.CalledProcessError(1, 'pydf')):
            total_disk, disk_free = system_monitor.get_rom_info()

            assert total_disk == 0.0
            assert disk_free == 0.0

    def test_get_rom_info_insufficient_lines(self, system_monitor):
        with patch('subprocess.run') as mock_run:
            mock_result = MagicMock()
            mock_result.stdout = "Filesystem"
            mock_run.return_value = mock_result
            total_disk, disk_free = system_monitor.get_rom_info()
            assert total_disk == 0.0
            assert disk_free == 0.0

    def test_get_rom_info_invalid_data_format(self, system_monitor):
        with patch('subprocess.run') as mock_run:
            mock_result = MagicMock()
            mock_result.stdout = "Filesystem\n/dev/sda1 Incomplete Data"
            mock_run.return_value = mock_result
            total_disk, disk_free = system_monitor.get_rom_info()
            assert total_disk == 0.0
            assert disk_free == 0.0

    def test_get_rom_info_value_conversion_error(self, system_monitor):
        with patch('subprocess.run') as mock_run:
            mock_result = MagicMock()
            mock_result.stdout = "Filesystem     Size   Used  Avail  Use%\n/dev/sda1    SizeG   UsedG   AvailG   50%"
            mock_run.return_value = mock_result
            total_disk, disk_free = system_monitor.get_rom_info()
            assert total_disk == 0.0
            assert disk_free == 0.0

    def test_get_rom_info_general_exception(self, system_monitor):
        with patch('subprocess.run', side_effect=Exception("Unexpected error")):
            total_disk, disk_free = system_monitor.get_rom_info()

            assert total_disk == 0.0
            assert disk_free == 0.0

    def test_collect_system_metrics_exception_handling(self, system_monitor):
        with patch.object(system_monitor, '_gather_system_metrics', side_effect=Exception("Test collect error")), \
                patch.object(system_monitor.logger, 'error') as mock_logger:
            system_monitor._collect_system_metrics()
            mock_logger.assert_called_once_with("Ошибка сбора системных метрик: Test collect error")

    def test_get_ram_info_exception_handling(self, system_monitor, caplog):
        caplog.set_level(logging.ERROR)
        caplog.clear()
        with patch('psutil.virtual_memory', side_effect=Exception("Test RAM error")), \
            patch.object(system_monitor.logger, 'error') as mock_logger:
            free_ram, total_ram = system_monitor.get_ram_info()
            assert free_ram == 0.0
            assert total_ram == 0.0
            mock_logger.assert_called_once_with("Ошибка получения RAM информации: Test RAM error")

    def test_gather_system_metrics_none_values_handling(self, system_monitor, caplog):
        caplog.set_level(logging.ERROR)
        caplog.clear()
        with patch('psutil.cpu_percent', return_value=None), \
                patch.object(system_monitor, 'get_ram_info', return_value=(None, None)), \
                patch.object(system_monitor, 'get_rom_info', return_value=(None, None)), \
                patch.object(system_monitor.logger, 'error') as mock_logger:
            result = system_monitor._gather_system_metrics()
            assert result == {}
            mock_logger.assert_called_once()
            assert "Ошибка получения системных метрик" in mock_logger.call_args[0][0]
