import img2pdf
import os
from PIL import Image
from contextlib import contextmanager
from src.domain import model


@contextmanager
def _open_jpg(img_path: str):
    try:
        image = Image.open(img_path)
        yield image
    finally:
        image.close()


@contextmanager
def _create_df(pdf_path: str, pdf_bytes: bytes):
    try:
        file = open(pdf_path, "wb")
        yield file
    finally:
        file.close()
