import sys
import logging
import pytest
from unittest.mock import MagicMock, patch
from PySide6.QtWidgets import QApplication, QMessageBox, QHeaderView
from PySide6.QtCore import Qt

from src.main import SystemPulse, main


class TestSystemPulse:
    @pytest.fixture
    def system_pulse_app(self, qtbot):
        app = SystemPulse()
        qtbot.addWidget(app)
        return app

    def test_init(self, system_pulse_app):
        assert system_pulse_app is not None
        assert system_pulse_app.ui is not None
        assert system_pulse_app.database_handler is not None
        assert system_pulse_app.system_monitor is not None

    def test_toggle_monitoring(self, system_pulse_app, qtbot):
        assert system_pulse_app.ui.pushButton_play.text() == "Начать запись"

        qtbot.mouseClick(system_pulse_app.ui.pushButton_play, Qt.LeftButton)
        assert system_pulse_app.ui.pushButton_play.text() == "Остановить"
        assert system_pulse_app.system_monitor.monitoring == True

        qtbot.mouseClick(system_pulse_app.ui.pushButton_play, Qt.LeftButton)
        assert system_pulse_app.ui.pushButton_play.text() == "Начать запись"
        assert system_pulse_app.system_monitor.monitoring == False

    def test_update_ui(self, system_pulse_app):
        test_metrics = {
            'cpu_percent': 50.0,
            'ram_free_mb': 4096,
            'ram_total_mb': 8192,
            'disk_free_gb': 100,
            'disk_total_gb': 500,
            'monitoring_time': '00:10:00'
        }

        system_pulse_app.update_ui(test_metrics)

        assert system_pulse_app.ui.progressBar_CPU.value() == 50
        assert system_pulse_app.ui.label_RAM_free.text() == "4096 МБ"
        assert system_pulse_app.ui.label_RAM_all.text() == "8192 МБ"
        assert system_pulse_app.ui.label_ROM_free.text() == "100 ГБ"
        assert system_pulse_app.ui.label_ROM_all.text() == "500 ГБ"
        assert system_pulse_app.ui.label_time.text() == "00:10:00"

    def test_reset_ui_metrics(self, system_pulse_app):
        system_pulse_app.ui.progressBar_CPU.setValue(75)
        system_pulse_app.ui.label_RAM_free.setText("2048 МБ")
        system_pulse_app.reset_ui_metrics()
        assert system_pulse_app.ui.progressBar_CPU.value() == 0
        assert system_pulse_app.ui.label_RAM_free.text() == "0 МБ"

    def test_update_timer_display(self, system_pulse_app):
        test_time = "00:15:30"
        system_pulse_app.update_timer_display(test_time)
        assert system_pulse_app.ui.label_time.text() == test_time

    def test_close_event(self, system_pulse_app):
        system_pulse_app.start_monitoring()
        mock_close_event = MagicMock()
        system_pulse_app.closeEvent(mock_close_event)
        assert system_pulse_app.system_monitor.monitoring == False
        mock_close_event.accept.assert_called_once()

    def test_update_system_metrics(self, system_pulse_app):
        metrics = {
            'cpu_percent': 50.5,
            'ram_free_mb': 4096,
            'ram_total_mb': 16384,
            'disk_free_gb': 500.25,
            'disk_total_gb': 1000,
            'monitoring_time': '00:10:30'
        }
        system_pulse_app._update_system_metrics(metrics)
        assert system_pulse_app.ui.progressBar_CPU.value() == 50
        assert system_pulse_app.ui.label_RAM_free.text() == "4096 МБ"
        assert system_pulse_app.ui.label_RAM_all.text() == "16384 МБ"
        assert system_pulse_app.ui.label_ROM_free.text() == "500.25 ГБ"
        assert system_pulse_app.ui.label_ROM_all.text() == "1000 ГБ"
        assert system_pulse_app.ui.label_time.text() == "00:10:30"

    def test_populate_table_row(self, system_pulse_app, qtbot):
        row_data = [1, 'Test', 3.14159, 42.5]
        system_pulse_app.ui.tableWidget_DB.setRowCount(0)
        system_pulse_app.ui.tableWidget_DB.setColumnCount(len(row_data))
        row_position = system_pulse_app.ui.tableWidget_DB.rowCount()
        system_pulse_app.ui.tableWidget_DB.insertRow(row_position)
        system_pulse_app._populate_table_row(row_position, row_data)
        for col, value in enumerate(row_data):
            item = system_pulse_app.ui.tableWidget_DB.item(row_position, col)
            assert item is not None, f"Элемент в столбце {col} не создан"

            if isinstance(value, float):
                assert item.text() == f"{value:.2f}"
            else:
                assert item.text() == str(value)

            assert item.textAlignment() == Qt.AlignCenter
        empty_row_data = []
        system_pulse_app.ui.tableWidget_DB.insertRow(row_position + 1)
        system_pulse_app._populate_table_row(row_position + 1, empty_row_data)
        assert system_pulse_app.ui.tableWidget_DB.rowCount() == row_position + 2

    def test_setup_table_widget(self, system_pulse_app, qtbot):
        system_pulse_app.setup_table_widget()
        header = system_pulse_app.ui.tableWidget_DB.horizontalHeader()
        last_column_index = header.count() - 1
        assert header.sectionResizeMode(last_column_index) == QHeaderView.Stretch

    def test_main_successful_execution(self):
        with patch('sys.argv', ['']), \
                patch('src.main.QApplication') as mock_qapp, \
                patch('src.main.SystemPulse') as mock_system_pulse, \
                patch('src.main.get_logger') as mock_logger:
            mock_app_instance = MagicMock()
            mock_qapp.return_value = mock_app_instance
            mock_app_instance.exec.return_value = 0
            mock_window = MagicMock()
            mock_system_pulse.return_value = mock_window
            result = main()
            mock_qapp.assert_called_once_with(sys.argv)
            mock_system_pulse.assert_called_once()
            mock_window.show.assert_called_once()
            mock_app_instance.exec.assert_called_once()
            assert result == 0

    def test_main_exception_handling(self, monkeypatch):
        with patch('sys.argv', ['']), \
                patch('src.main.QApplication') as mock_qapp, \
                patch('src.main.SystemPulse', side_effect=Exception("Test Error")) as mock_system_pulse, \
                patch('src.main.get_logger') as mock_logger, \
                patch('sys.exit') as mock_sys_exit:
            mock_app_instance = MagicMock()
            mock_qapp.return_value = mock_app_instance
            mock_logger_instance = MagicMock()
            mock_logger.return_value = mock_logger_instance
            main()
            mock_logger_instance.error.assert_called_once()
            mock_sys_exit.assert_called_once_with(1)

    def test_main_application_creation(self, monkeypatch):
        existing_app = QApplication.instance()
        if existing_app:
            existing_app.quit()
            del existing_app
        with patch('sys.argv', ['']), \
                patch('src.main.QApplication') as mock_qapp, \
                patch('src.main.SystemPulse') as mock_system_pulse, \
                patch('sys.exit') as mock_sys_exit:
            mock_app_instance = MagicMock()
            mock_qapp.return_value = mock_app_instance
            mock_app_instance.exec.return_value = 0
            result = main()
            mock_qapp.assert_called_once_with(sys.argv)
            mock_system_pulse.assert_called_once()
            mock_app_instance.exec.assert_called_once()
            assert result == 0

    def test_stop_monitoring_if_active(self, system_pulse_app):
        system_pulse_app.start_monitoring()
        assert system_pulse_app.system_monitor.monitoring == True
        system_pulse_app._stop_monitoring_if_active()
        assert system_pulse_app.system_monitor.monitoring == False

    def test_populate_table_row_empty_data(self, system_pulse_app):
        empty_row_data = []
        row_position = system_pulse_app.ui.tableWidget_DB.rowCount()
        system_pulse_app.ui.tableWidget_DB.insertRow(row_position)
        system_pulse_app._populate_table_row(row_position, empty_row_data)
        assert system_pulse_app.ui.tableWidget_DB.item(row_position, 0) is None

    def test_clear_database_confirmation(self, system_pulse_app, monkeypatch):
        system_pulse_app.start_monitoring()
        monkeypatch.setattr(QMessageBox, 'question', lambda *args: QMessageBox.Yes)
        system_pulse_app.clear_database()
        assert system_pulse_app.system_monitor.monitoring == False
        assert system_pulse_app.ui.pushButton_play.text() == "Начать запись"

    def test_clear_database_cancellation(self, system_pulse_app, monkeypatch):
        monkeypatch.setattr(QMessageBox, 'question', lambda *args: QMessageBox.No)
        system_pulse_app.start_monitoring()
        system_pulse_app.clear_database()
        assert system_pulse_app.system_monitor.monitoring == True

    def test_setup_table_widget_resize(self, system_pulse_app):
        mock_event = MagicMock()
        system_pulse_app.setup_table_widget()
        system_pulse_app.ui.tableWidget_DB.resizeEvent(mock_event)
        header = system_pulse_app.ui.tableWidget_DB.horizontalHeader()
        last_column_index = header.count() - 1
        assert header.sectionResizeMode(last_column_index) == QHeaderView.Stretch

    def test_show_database_metrics_population(self, system_pulse_app, monkeypatch):
        test_metrics = [
            (1, '2024-01-15', 'CPU', 50.5, 'Test1'),
            (2, '2024-01-16', 'RAM', 60.7, 'Test2')
        ]

        def mock_get_all_metric():
            return test_metrics

        monkeypatch.setattr(system_pulse_app.database_handler, 'get_all_metric', mock_get_all_metric)
        mock_populate_calls = []

        def mock_populate_table_row(row_position, row_data):
            mock_populate_calls.append((row_position, row_data))

        monkeypatch.setattr(system_pulse_app, '_populate_table_row', mock_populate_table_row)
        system_pulse_app.show_database_metrics()
        assert len(mock_populate_calls) == len(test_metrics), "Должны быть заполнены все строки"
        for i, (row_position, row_data) in enumerate(mock_populate_calls):
            assert row_position == i, f"Неверная позиция строки для записи {i}"
            assert row_data == list(test_metrics[i]), f"Неверные данные для строки {i}"

    def test_show_database_metrics_empty(self, system_pulse_app, monkeypatch):
        monkeypatch.setattr(system_pulse_app.database_handler, 'get_all_metric', lambda: [])
        mock_populate_calls = []
        def mock_populate_table_row(row_position, row_data):
            mock_populate_calls.append((row_position, row_data))
        monkeypatch.setattr(system_pulse_app, '_populate_table_row', mock_populate_table_row)
        system_pulse_app.ui.tableWidget_DB.setRowCount(0)
        system_pulse_app.show_database_metrics()
        assert len(mock_populate_calls) == 0, "Не должно быть попыток заполнения при пустой базе"
        assert system_pulse_app.ui.tableWidget_DB.rowCount() == 0, "Таблица должна остаться пустой"

    def test_show_database_metrics_exception_handling(self, system_pulse_app, caplog):
        caplog.set_level(logging.ERROR)
        with patch.object(system_pulse_app.database_handler, 'get_all_metric',
                          side_effect=Exception("Тестовая ошибка базы данных")), \
                patch.object(system_pulse_app.ui.tableWidget_DB, 'setRowCount') as mock_set_row_count, \
                patch.object(system_pulse_app, 'logger') as mock_logger:
            system_pulse_app.show_database_metrics()
            mock_set_row_count.assert_called_once_with(0)
            mock_logger.error.assert_called_once_with(
                "Ошибка отображения метрик: Тестовая ошибка базы данных",
                exc_info=True
            )
