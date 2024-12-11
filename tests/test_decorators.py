from typing import Any

import pytest

from src.decorators import log


@log()
def successful_function(x: int, y: int) -> int:
    """Функция для успешного выполнения."""
    return x + y


@log()
def error_function(x: int, y: int) -> float:
    """Функция, которая вызывает ошибку деления на ноль."""
    return x / y


def test_success_log(capsys: Any) -> None:
    """Тестируем успешное выполнение функции."""
    successful_function(3, 4)
    captured = capsys.readouterr()

    assert "successful_function is ok" in captured.out


def test_error_log(capsys: Any) -> None:
    """Тестируем обработку ошибки в функции."""
    with pytest.raises(ZeroDivisionError):
        error_function(1, 0)

    captured = capsys.readouterr()
    assert "error_function error: division by zero" in captured.out
    assert "input: (1, 0), {}" in captured.out


def test_log_to_file(tmp_path: Any) -> None:
    """Тестируем запись логов в файл."""
    log_file = tmp_path / "test_log.txt"
    func = log(filename=str(log_file))(successful_function)
    func(5, 7)

    with open(log_file) as f:
        log_contents = f.read()

    assert "successful_function is ok" in log_contents


def test_error_log_to_file(tmp_path: Any) -> None:
    """Тестируем запись логов ошибок в файл."""
    log_file = tmp_path / "test_error_log.txt"
    func = log(filename=str(log_file))(error_function)

    with pytest.raises(ZeroDivisionError):
        func(1, 0)

    with open(log_file) as f:
        log_contents = f.read()

    assert "error_function error: division by zero" in log_contents
    assert "input: (1, 0), {}" in log_contents
