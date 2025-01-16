import pytest
import sqlite3
from unittest.mock import patch

from src.database import DatabaseHandler


class TestDatabaseHandler:
    @pytest.fixture
    def temp_db_path(self, tmp_path):
        db_path = tmp_path / "test_database.db"
        return str(db_path)

    @pytest.fixture
    def database_handler(self, temp_db_path):
        return DatabaseHandler(db_name=temp_db_path)

    def test_initialization(self, temp_db_path):
        handler = DatabaseHandler(db_name=temp_db_path)
        assert handler.db_name == temp_db_path
        assert handler.logger is not None

    def test_get_connection_success(self, database_handler):
        connection = database_handler._get_connection()
        assert isinstance(connection, sqlite3.Connection)
        connection.close()

    def test_get_connection_error(self):
        with patch('sqlite3.connect', side_effect=sqlite3.Error("Test error")):
            with pytest.raises(sqlite3.Error):
                DatabaseHandler(db_name="/nonexistent/path/database.db")._get_connection()

    def test_validate_metrics_success(self):
        handler = DatabaseHandler()
        valid_metrics = {
            'time_lapse': 1,
            'monitoring_time': '00:10:00',
            'cpu_percent': 50.5,
            'ram_free_mb': 1024.0,
            'ram_total_mb': 8192.0,
            'disk_free_gb': 100.5,
            'disk_total_gb': 500.0
        }
        assert handler._validate_metrics(valid_metrics) is True

    def test_validate_metrics_missing_keys(self):
        handler = DatabaseHandler()
        invalid_metrics = {
            'time_lapse': 1,
            'monitoring_time': '00:10:00'
        }
        assert handler._validate_metrics(invalid_metrics) is False

    def test_validate_metrics_invalid_types(self):
        handler = DatabaseHandler()
        invalid_metrics = {
            'time_lapse': 1,
            'monitoring_time': '00:10:00',
            'cpu_percent': 'invalid',
            'ram_free_mb': 'test',
            'ram_total_mb': 8192.0,
            'disk_free_gb': 100.5,
            'disk_total_gb': 500.0
        }
        assert handler._validate_metrics(invalid_metrics) is False

    def test_create_table(self, database_handler):
        database_handler.create_table()
        with database_handler._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='system_metrics'")
            table_exists = cursor.fetchone()

        assert table_exists is not None

    def test_adding_data_success(self, database_handler):
        metrics = {
            'time_lapse': 1,
            'monitoring_time': '00:10:00',
            'cpu_percent': 50.5,
            'ram_free_mb': 1024.0,
            'ram_total_mb': 8192.0,
            'disk_free_gb': 100.5,
            'disk_total_gb': 500.0
        }
        result = database_handler.adding_data(metrics)
        assert result is True

    def test_adding_data_invalid_metrics(self, database_handler):
        invalid_metrics = {}
        result = database_handler.adding_data(invalid_metrics)
        assert result is False

    def test_adding_data_database_error(self, database_handler):
        metrics = {
            'time_lapse': 1,
            'monitoring_time': '00:10:00',
            'cpu_percent': 50.5,
            'ram_free_mb': 1024.0,
            'ram_total_mb': 8192.0,
            'disk_free_gb': 100.5,
            'disk_total_gb': 500.0
        }

        with patch.object(database_handler, '_get_connection', side_effect=sqlite3.Error):
            result = database_handler.adding_data(metrics)
            assert result is False

    def test_get_all_metric(self, database_handler):
        metrics = {
            'time_lapse': 1,
            'monitoring_time': '00:10:00',
            'cpu_percent': 50.5,
            'ram_free_mb': 1024.0,
            'ram_total_mb': 8192.0,
            'disk_free_gb': 100.5,
            'disk_total_gb': 500.0
        }
        database_handler.adding_data(metrics)
        all_metrics = database_handler.get_all_metric()
        assert len(all_metrics) > 0

    def test_get_all_metric_error(self, database_handler):
        with patch('sqlite3.connect', side_effect=sqlite3.Error):
            all_metrics = database_handler.get_all_metric()
            assert all_metrics == []

    def test_clear_all_metric(self, database_handler):
        metrics = {
            'time_lapse': 1,
            'monitoring_time': '00:10:00',
            'cpu_percent': 50.5,
            'ram_free_mb': 1024.0,
            'ram_total_mb': 8192.0,
            'disk_free_gb': 100.5,
            'disk_total_gb': 500.0
        }
        database_handler.adding_data(metrics)
        result = database_handler.clear_all_metric()
        assert result is True
        all_metrics = database_handler.get_all_metric()
        assert len(all_metrics) == 0

    def test_clear_all_metric_error(self, database_handler):
        with patch('sqlite3.connect', side_effect=sqlite3.Error("Test error")):
            metrics = {
                'time_lapse': 1,
                'monitoring_time': '00:10:00',
                'cpu_percent': 50.5,
                'ram_free_mb': 1024.0,
                'ram_total_mb': 8192.0,
                'disk_free_gb': 100.5,
                'disk_total_gb': 500.0
            }
            database_handler.adding_data(metrics)
            result = database_handler.clear_all_metric()
            assert result is False

    def test_clear_all_metric_with_no_table(self, database_handler):
        with database_handler._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DROP TABLE IF EXISTS system_metrics")
            conn.commit()

        result = database_handler.clear_all_metric()
        assert result is True

        with database_handler._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='system_metrics'")
            table_exists = cursor.fetchone()
            assert table_exists is not None
