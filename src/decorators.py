from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор, логирующий работу функции и её результат в консоль"""

    def logging_decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)

                log_message = f"{func.__name__} is ok, Result: {result}"

                if filename:
                    with open(filename, "a") as file:
                        file.write(log_message + "\n")
                else:
                    print(log_message)

                return result

            except Exception as error_:
                log_message = f"{func.__name__} error: {error_}, input: {args}, {kwargs}"

                if filename:
                    with open(filename, "a") as file:
                        file.write(log_message + "\n")
                else:
                    print(log_message)

                raise

        return wrapper

    return logging_decorator
