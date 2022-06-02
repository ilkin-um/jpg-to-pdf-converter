from re import L
import pytest
import uuid
import sys

sys.path.append(r"C:\Users\pythondev\Desktop\personal\portfolio\jpeg-to-pdf-converter")
from src.entrypoints.api.app import create_app


@pytest.fixture
def app():
    return create_app("testing")


@pytest.fixture
def get_uuid():
    return uuid.uuid4()


@pytest.fixture
def get_jpg_dict(get_uuid):
    return {"code": get_uuid, "src_path": "random.jpg"}


@pytest.fixture
def get_pdf_dict(get_uuid):
    return {"code": get_uuid, "destination_path": "random.pdf"}
