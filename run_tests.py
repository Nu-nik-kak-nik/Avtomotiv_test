import os
import sys
import pytest


def run_tests():
    project_root = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, project_root)

    try:
        result = pytest.main([
            'tests',
            '-v',
            '--cov=src',
            '--cov-report=term-missing'
        ])

        if result == pytest.ExitCode.OK:
            print("✅ Все тесты пройдены успешно!")
        elif result == pytest.ExitCode.TESTS_FAILED:
            print("❌ Некоторые тесты не пройдены!")
        else:
            print(f"❗ При тестировании возникла проблема (Код завершения: {result})")
        return result == 0
    finally:
        sys.path.pop(0)


def main():
    success = run_tests()
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
