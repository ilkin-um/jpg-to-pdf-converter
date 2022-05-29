import pytest
import sys
import uuid
sys.path.append(r"C:\Users\pythondev\Desktop\personal\portfolio\jpeg-to-pdf-converter")
from src.domain import model
from src.domain.exception import WrongFileExtensionException


def test_jpeg_creation(get_uuid):
    jpeg = model.JPG(code=get_uuid,src_path="test.jpg")
    assert jpeg.extensions == (".jpg", ".jpeg")


def test_if_jpegs_are_equal(get_uuid):
    jpg1 = model.JPG(code=get_uuid,src_path="test.jpg")
    jpg2 = model.JPG(code=get_uuid,src_path="test.jpg")

    assert jpg1 == jpg2


def test_pdf_creation(get_uuid):
    pdf = model.PDF(code=get_uuid,destination_path="test.pdf")
    assert pdf.extension == (".pdf")


def test_if_pdfs_are_equal(get_uuid):
    pdf1 = model.PDF(code=get_uuid,destination_path="test.pdf")
    pdf2 = model.PDF(code=get_uuid,destination_path="test.pdf")

    assert pdf1 == pdf2


def test_jpeg_allocation(get_uuid):
    jpeg = model.JPG(code=get_uuid,src_path="test.jpg")
    assert model.allocate_jpeg(code=get_uuid,src_path="test.jpg") == jpeg


def test_pdf_allocation(get_uuid):
    pdf = model.PDF(code=get_uuid,destination_path="test.pdf")
    assert model.allocate_pdf(code=get_uuid,destination_path="test.pdf") == pdf


def test_jpeg_allocation_wrong_extension(get_uuid):
    with pytest.raises(WrongFileExtensionException) as err:
        model.allocate_jpeg(code=get_uuid,src_path="test.mp4")

    assert str(err.value) == "Expected file with .jpg or .jpeg extension, got another."


def test_pdf_allocation_wrong_extension(get_uuid):
    with pytest.raises(WrongFileExtensionException) as err:
        model.allocate_pdf(code=get_uuid,destination_path="test.svg")

    assert str(err.value) == "Expected file with .pdf extension, got another."
