import img2pdf
from PIL import Image
from contextlib import contextmanager
from src.domain import model
from src.service import validator
from typing import Generator
import uuid

@contextmanager
def _open_jpg(img_path: str) -> Generator:
    try:
        image = Image.open(img_path)
        yield image
    finally:
        image.close()


@validator.is_pdf_path_valid
@contextmanager
def _create_pdf(pdf_path: str) -> Generator:
    try:
        file = open(pdf_path, "wb")
        yield file
    finally:
        file.close()


def _convert_and_save_pdf(image, pdf) -> None:
    pdf_bytes = _convert_to_pdf(image)

    with _create_pdf(pdf.destination_path) as file:
        file.write(pdf_bytes)


def _convert_to_pdf(image) -> bytes:
    return img2pdf.convert(image.filename)


def _get_jpg_and_pdf(jpg_path, pdf_path) -> tuple[model.JPG, model.PDF]:
    jpg = model.allocate_jpeg(code=uuid.uuid4(),src_path=jpg_path)
    pdf = model.allocate_pdf(code=uuid.uuid4(),destination_path=pdf_path)
    return jpg, pdf


@validator.is_jpg_path_valid
def jpg2pdf(jpg_path: str, pdf_path: str) -> None:
    jpg, pdf = _get_jpg_and_pdf(jpg_path, pdf_path)
    with _open_jpg(jpg.src_path) as img:
        _convert_and_save_pdf(img, pdf)
