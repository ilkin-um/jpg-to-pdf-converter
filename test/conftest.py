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
