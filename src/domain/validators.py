from functools import wraps
from src.domain.exceptions import WrongFileExtensionException


def is_jpeg(src: str) -> bool:
    return src.endswith(".jpg") or src.endswith(".jpeg")


def is_pdf(func: callable) -> callable:
    @wraps(func)
    def wrapper(destination_path):
        if destination_path.endswith(".pdf"):
            return func(destination_path=destination_path)
        raise WrongFileExtensionException(
            "Expected file with .pdf extension, got another."
        )

    return wrapper
