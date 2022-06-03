import os
import pytest
from src.service import converter
from src.domain.exception import WrongFileExtensionException


def test_jpeg_to_pdf_conversion():
    jpg_path = os.path.abspath("test/data/random.jpg")
    pdf_path = os.path.abspath("test/data/random.pdf")
    converter.jpg2pdf(jpg_path, pdf_path)
    assert os.path.isfile(pdf_path)


def test_with_wrong_jpg_path():
    jpg_path = os.path.abspath("./notexists/random.jpg")
    pdf_path = os.path.abspath("test/data/random.pdf")
    with pytest.raises(FileNotFoundError) as err:
        converter.jpg2pdf(jpg_path, pdf_path)
    assert str(err.value) == "Path to jpeg file is wrong"


def test_with_wrong_pdf_path():
    jpg_path = os.path.abspath("test/data/random.jpg")
    pdf_path = os.path.abspath("test/notexists/random.pdf")
    with pytest.raises(FileNotFoundError) as err:
        converter.jpg2pdf(jpg_path, pdf_path)
    assert str(err.value) == "Path to pdf file is wrong"


def test_with_wrong_format():
    jpg_path = os.path.abspath("test/data/random.txt")
    pdf_path = os.path.abspath("test/asdsad/random.pdf")
    with pytest.raises(WrongFileExtensionException) as err:
        converter.jpg2pdf(jpg_path, pdf_path)
    assert str(err.value) == "Expected file with .jpg or .jpeg extension, got another."


def test_return_value_of_convertion():
    jpg_path = os.path.abspath("test/data/random.jpg")
    pdf_path = os.path.abspath("test/data/random.pdf")
    converted = converter.jpg2pdf(jpg_path, pdf_path)
    assert converted.converted_from.src_path == jpg_path
    assert converted.converted_to.destination_path == pdf_path
