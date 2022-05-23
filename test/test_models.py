import pytest
import sys

sys.path.append(r"C:\Users\pythondev\Desktop\personal\portfolio\jpeg-to-pdf-converter")
from src.domain import model


def test_jpeg_creation():
    jpeg = model.JPG(src_path="test.jpg")
    assert jpeg.extensions == (".jpg", ".jpeg")


def test_jpegs_are_equal():
    jpg1 = model.JPG(src_path="test.jpg")
    jpg2 = model.JPG(src_path="test.jpg")

    assert jpg1 == jpg2
