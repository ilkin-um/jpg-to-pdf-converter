import pytest
import sys

sys.path.append(r"C:\Users\pythondev\Desktop\personal\portfolio\jpeg-to-pdf-converter")
from src.domain import model
from src.domain.exceptions import WrongFileExtensionException


def test_jpeg_creation():
    jpeg = model.JPG(src_path="test.jpg")
    assert jpeg.extensions == (".jpg", ".jpeg")


def test_if_jpegs_are_equal():
    jpg1 = model.JPG(src_path="test.jpg")
    jpg2 = model.JPG(src_path="test.jpg")

    assert jpg1 == jpg2


def test_pdf_creation():
    pdf = model.PDF(destination_path="test.pdf")
    assert pdf.extension == (".pdf")


def test_if_jpdfs_are_equal():
    pdf1 = model.PDF(destination_path="test.pdf")
    pdf2 = model.PDF(destination_path="test.pdf")

    assert pdf1 == pdf2


def test_jeg_allocation():
    jpeg = model.JPG(src_path="test.jpg")
    assert model.allocate_jpeg(src_path="test.jpg") == jpeg


def test_pdf_allocation():
    pdf = model.PDF(destination_path="test.pdf")
    assert model.allocate_pdf(destination_path="test.pdf") == pdf


def test_jpeg_allocation_wrong_extension():
    with pytest.raises(WrongFileExtensionException) as err:
        model.allocate_jpeg(src_path="test.mp4")

    assert str(err.value) == "Expected file with .jpg or .jpeg extension, got another."


def test_pdf_allocation_wrong_extension():
    with pytest.raises(WrongFileExtensionException) as err:
        model.allocate_pdf(destination_path="test.svg")

    assert str(err.value) == "Expected file with .pdf extension, got another."
