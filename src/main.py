import sys
import os
from typing import Dict, Any

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QTableWidgetItem,
    QHeaderView, QAbstractItemView, QMessageBox
)
from PySide6.QtGui import QCloseEvent

from src.UI.design import Ui_SystemPulse
from src.system_monitor import SystemMonitor
from src.database import DatabaseHandler
from src.logger_config import get_logger
from src.system_info import SystemInfo

class SystemPulse(QMainWindow):

    def __init__(self):
        try:
            super(SystemPulse, self).__init__()
            self.logger = get_logger(self.__class__.__name__)

            self._init_ui()
            self._init_system_components()
            self._setup_connections()
            self._post_init_setup()

            self.logger.info("Инициализация SystemPulse завершена успешно")

        except Exception as e:
            self.logger.critical(f"Ошибка инициализации: {e}")

    def _init_ui(self):
        self.ui = Ui_SystemPulse()
        self.ui.setupUi(self)
        self.ui.tableWidget_DB.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def _init_system_components(self):
        self.database_handler = DatabaseHandler()
        self.system_monitor = SystemMonitor()
        self.system_info = SystemInfo()

    def _setup_connections(self):
        self.system_monitor.update_metrics.connect(self.update_ui)
        self.system_monitor.update_timer.connect(self.update_timer_display)

        self.ui.spinBox_update_interval.valueChanged.connect(self.system_monitor.set_time_lapse)
        self.ui.pushButton_play.clicked.connect(self.toggle_monitoring)
        self.ui.pushButton_remove.clicked.connect(self.clear_database)

    def _post_init_setup(self):
        QTimer.singleShot(100, self.setup_table_widget)
        self.show_database_metrics()
        self.output_of_system_info()

    def update_timer_display(self, time_str):
        """Обновление отображения времени таймера"""
        self.ui.label_time.setText(time_str)

    def toggle_monitoring(self):
        """Переключает состояние мониторинга и обновляет текст кнопки"""
        button_text = self.ui.pushButton_play.text()

        if button_text == "Начать запись":
            self.start_monitoring()
            self.ui.pushButton_play.setText("Остановить")
        else:
            self.stop_monitoring()
            self.ui.pushButton_play.setText("Начать запись")

    def start_monitoring(self):
        """Запуск мониторинга"""
        self.system_monitor.start_monitoring()

    def stop_monitoring(self):
        """Остановка мониторинга"""
        self.system_monitor.stop_monitoring()
        self.reset_ui_metrics()

    def update_ui(self, metrics: Dict[str, Any]):
        """Обновление UI данными"""
        self._update_system_metrics(metrics)
        self.show_database_metrics()

    def _update_system_metrics(self, metrics: Dict[str, Any]):
        """Обновление системных метрик в UI"""
        # --------------------------------------------------------------------------------------------------------------
        self.ui.progressBar_CPU.setValue(int(metrics['cpu_percent']))
        self.ui.progressBar_GPU.setValue(int(metrics['gpu_load']))
        self.ui.label_RAM_free.setText(f"{metrics['ram_free_mb']} МБ")
        self.ui.label_RAM_all.setText(f"{metrics['ram_total_mb']} МБ")
        self.ui.label_ROM_free.setText(f"{metrics['disk_free_gb']} ГБ")
        self.ui.label_ROM_all.setText(f"{metrics['disk_total_gb']} ГБ")
        self.ui.label_time.setText(metrics['monitoring_time'])

    def show_database_metrics(self):
        """Отображение сохраненных метрик в таблице"""
        self.ui.tableWidget_DB.setRowCount(0)
        try:
            metrics = self.database_handler.get_all_metric()
            if not metrics:
                return

            for row_data in metrics:
                row_position = self.ui.tableWidget_DB.rowCount()
                self.ui.tableWidget_DB.insertRow(row_position)
                self._populate_table_row(row_position, list(row_data))

        except Exception as e:
            self.logger.error(f"Ошибка отображения метрик: {e}", exc_info=True)

    def _populate_table_row(self, row_position: int, row_data: list):
        """Заполнение строки таблицы данными"""
        for col, value in enumerate(row_data):
            str_value = f"{value:.2f}" if isinstance(value, float) else str(value)
            item = QTableWidgetItem(str_value)
            item.setTextAlignment(Qt.AlignCenter)
            self.ui.tableWidget_DB.setItem(row_position, col, item)

    def reset_ui_metrics(self):
        """Сброс метрик в интерфейсе"""
        # --------------------------------------------------------------------------------------------------------------
        metrics_reset = {
            'progressBar_CPU': 0,
            'progressBar_GPU': 0,
            'label_RAM_free': "0 МБ",
            'label_RAM_all': "0 МБ",
            'label_ROM_free': "0 ГБ",
            'label_ROM_all': "0 ГБ",
            'label_time': ""
        }

        for attr, value in metrics_reset.items():
            if hasattr(getattr(self.ui, attr), 'setText'):
                getattr(self.ui, attr).setText(value)
            else:
                getattr(self.ui, attr).setValue(value)

    def clear_database(self):
        """Очистка базы данных и обновление таблицы"""
        reply = QMessageBox.question(
            self,
            'Очистка базы данных',
            'Вы уверены, что хотите очистить базу данных?',
            QMessageBox.Yes | QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            if self.system_monitor.monitoring:
                self.stop_monitoring()
                self.ui.pushButton_play.setText("Начать запись")

            self.database_handler.clear_all_metric()
            self.show_database_metrics()
            self.reset_ui_metrics()

    def setup_table_widget(self):
        """Настройка внешнего вида таблицы"""
        header = self.ui.tableWidget_DB.horizontalHeader()
        header.setStretchLastSection(True)
        last_column_index = header.count() - 1

        def resize_last_column():
            table_width = self.ui.tableWidget_DB.width()
            last_column_width = max(table_width * 0.2, 150)
            self.ui.tableWidget_DB.setColumnWidth(last_column_index, int(last_column_width))

        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        header.setSectionResizeMode(last_column_index, QHeaderView.Stretch)
        self.ui.tableWidget_DB.resizeEvent = lambda event: resize_last_column()
        resize_last_column()

    def closeEvent(self, event: QCloseEvent):
        """Обработка закрытия окна"""
        self._stop_monitoring_if_active()
        event.accept()

    def _stop_monitoring_if_active(self):
        """Остановка мониторинга при активном процессе"""
        if getattr(self.system_monitor, 'monitoring', False):
            self.stop_monitoring()

    def output_of_system_info(self):
        """Заполнение полей интерфейса системной информацией."""
        try:
            ui_mapping = {
                'OS': self.ui.lineEdit_OS,
                'Hostname': self.ui.lineEdit_Hostname,
                'Desktop Environment': self.ui.lineEdit_DE,
                'Kernel': self.ui.lineEdit_Kernel,
                'CPU': self.ui.lineEdit_CPU,
                'Architecture': self.ui.lineEdit_Architecture
            }

            system_info = self.system_info.collect_system_info()

            for key, ui_element in ui_mapping.items():
                value = system_info.get(key, 'N/A')
                ui_element.setText(value)

        except Exception as e:
            self.logger.error(f"Ошибка при выводе системной информации: {e}")

def main():
    """Точка входа в приложение"""
    logger = get_logger('MainApplication')
    try:
        app = QApplication(sys.argv)
        window = SystemPulse()
        window.show()
        result = app.exec()
        if __name__ == '__main__':
            sys.exit(result)
        return result

    except Exception as e:
        logger.error(f"Критическая ошибка приложения: {e}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    sys.exit(main())