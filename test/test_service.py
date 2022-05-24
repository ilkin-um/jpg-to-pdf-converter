import os
from src.service import converter


def test_jpeg_to_pdf_conversion():
    jpg_path = os.path.abspath("test/data/random.jpg")
    pdf_path = os.path.abspath("test/data/random.pdf")
    converter.jpg2pdf(jpg_path, pdf_path)
    assert os.path.isfile(pdf_path)
