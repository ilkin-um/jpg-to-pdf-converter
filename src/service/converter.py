import img2pdf
import os
from PIL import Image
from contextlib import contextmanager
from src.domain import model


def _convert_and_save_pd(image, pdf):
    pdf_bytes = img2pdf.convert(image.filename)

    with _create_pdf(pdf.destination_path, pdf_bytes) as file:
        file.write(pdf_bytes)


def _get_jpg_and_pdf(jpg_path, pdf_path):
    jpg = model.JPG(src_path=jpg_path)
    pdf = model.PDF(destination_path=pdf_path)
    return jpg, pdf


@contextmanager
def _open_jpg(img_path: str):
    try:
        image = Image.open(img_path)
        yield image
    finally:
        image.close()


@contextmanager
def _create_pdf(pdf_path: str, pdf_bytes: bytes):
    try:
        file = open(pdf_path, "wb")
        yield file
    finally:
        file.close()
