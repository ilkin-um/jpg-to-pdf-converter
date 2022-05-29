from functools import wraps
from src.domain.exception import WrongFileExtensionException


def is_jpeg(func: callable) -> callable:
    @wraps(func)
    def wrapper(code,src_path):
        if src_path.endswith(".jpg") or src_path.endswith(".jpeg"):
            return func(code=code,src_path=src_path)
        raise WrongFileExtensionException(
            "Expected file with .jpg or .jpeg extension, got another."
        )

    return wrapper


def is_pdf(func: callable) -> callable:
    @wraps(func)
    def wrapper(code,destination_path):
        if destination_path.endswith(".pdf"):
            return func(code=code,destination_path=destination_path)
        raise WrongFileExtensionException(
            "Expected file with .pdf extension, got another."
        )

    return wrapper
