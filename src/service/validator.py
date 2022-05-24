import os
from functools import wraps


def is_jpg_path_valid(func):
    @wraps(func)
    def wrapper(jpg_path: str, _: str):
        if not os.path.isfile(jpg_path):
            raise FileNotFoundError("Path does not include jpeg file")
        return func(jpg_path, _)

    return wrapper


def is_pdf_path_valid(func):
    @wraps(func)
    def wrapper(pdf_path):
        if not os.path.exists(os.path.dirname(pdf_path)):
            raise FileNotFoundError("Wrong pdf file path provided")
        return func(pdf_path)

    return wrapper
