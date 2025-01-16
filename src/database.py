import sqlite3
from datetime import datetime
from typing import Dict, Any, List
from src.logger_config import get_logger


class DatabaseHandler:
    def __init__(self, db_name='system_monitoring.db'):
        self.logger = get_logger(self.__class__.__name__)
        self.logger.info(f"Инициализация базы данных: {db_name}")

        self.db_name = db_name
        self.create_table()

    def _get_connection(self) -> sqlite3.Connection:
        """Создание соединения с базой данных"""
        try:
            conn = sqlite3.connect(self.db_name)
            return conn
        except sqlite3.Error as e:
            self.logger.error(f"Ошибка при подключении к базе данных: {e}")
            raise

    def _validate_metrics(self, metrics: Dict[str, Any]) -> bool:
        """Валидация входящих метрик"""
        required_keys = [
            'time_lapse', 'monitoring_time', 'cpu_percent',
            'ram_free_mb', 'ram_total_mb', 'disk_free_gb', 'disk_total_gb'
        ]

        if not all(key in metrics for key in required_keys):
            return False

        try:
            float(metrics['cpu_percent'])
            float(metrics['ram_free_mb'])
            float(metrics['ram_total_mb'])
            float(metrics['disk_free_gb'])
            float(metrics['disk_total_gb'])
            int(metrics['time_lapse'])
        except (ValueError, TypeError):
            self.logger.error(f"Неверный тип данных в метриках: {metrics}")
            return False

        return True

    def create_table(self) -> None:
        """Создание таблицы для хранения системных метрик"""
        try:
            with self._get_connection() as conn:
                            cursor = conn.cursor()
                            cursor.execute('''
                                CREATE TABLE IF NOT EXISTS system_metrics (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    time_lapse INTEGER,
                                    timestamp DATE,
                                    monitoring_time TEXT,
                                    cpu_percent REAL,
                                    ram_free_mb REAL,
                                    ram_total_mb REAL,
                                    disk_free_gb REAL,
                                    disk_total_gb REAL
                                )
                            ''')
                            conn.commit()
        except sqlite3.Error:
            pass

    def adding_data(self, metrics: Dict[str, Any]) -> bool:
        """Добавление метрик в базу данных"""
        if not self._validate_metrics(metrics):
            return False

        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                            INSERT INTO system_metrics (
                                time_lapse, 
                                timestamp,
                                monitoring_time, 
                                cpu_percent, 
                                ram_free_mb, 
                                ram_total_mb, 
                                disk_free_gb, 
                                disk_total_gb
                            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                        ''', (
                    metrics['time_lapse'],
                    datetime.now().strftime('%Y-%m-%d'),
                    metrics['monitoring_time'],
                    metrics['cpu_percent'],
                    metrics['ram_free_mb'],
                    metrics['ram_total_mb'],
                    metrics['disk_free_gb'],
                    metrics['disk_total_gb']
                ))
                conn.commit()
                self.logger.info("Метрики успешно добавлены")
                return True
        except sqlite3.Error as e:
            self.logger.error(f"Ошибка при добавлении метрик: {e}")
            return False

    def get_all_metric(self) -> List[tuple]:
        """Получение всех метрик из базы данных"""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM system_metrics')
                metrics = cursor.fetchall()
                self.logger.info(f"Получено {len(metrics)} записей")
                return metrics
        except sqlite3.Error:
            return []

    def clear_all_metric(self) -> bool:
        """Очистка всех метрик из базы данных"""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='system_metrics'")
                table_exists = cursor.fetchone()

                if table_exists:
                    cursor.execute('DELETE FROM system_metrics')
                else:
                    self.create_table()

                conn.commit()
                self.logger.info("Все метрики удалены")
                return True
        except sqlite3.Error as e:
            self.logger.error(f"Ошибка при очистке метрик: {e}")
            return False
