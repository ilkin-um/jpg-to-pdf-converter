from re import L
import pytest
import uuid
import sys
import datetime

sys.path.append(r"C:\Users\pythondev\Desktop\personal\portfolio\jpeg-to-pdf-converter")
from src.entrypoints.api.app import create_app
from src.domain import model


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


@pytest.fixture
def converted_data(get_uuid):
    jpg = model.JPG(code=get_uuid, src_path="random.jpg")
    pdf = model.PDF(code=get_uuid, destination_path="random.pdf")
    converted_1 = model.Converted(
        converted_from=jpg, converted_to=pdf, converted_at=datetime.datetime.now()
    )
    converted_2 = model.Converted(
        converted_from=jpg, converted_to=pdf, converted_at=datetime.datetime.now()
    )
    converted_3 = model.Converted(
        converted_from=jpg, converted_to=pdf, converted_at=datetime.datetime.now()
    )

    return [converted_1, converted_2, converted_3]


@pytest.fixture
def converted_dicts(get_uuid):
    jpg = model.JPG(code=get_uuid, src_path="fake.jpg")
    pdf = model.PDF(code=get_uuid, dest_path="fake.pdf")
    return [
        {
            "converted_from": jpg,
            "converted_to": pdf,
            "converted_at": datetime.datetime.now(),
        },
        {
            "converted_from": jpg,
            "converted_to": pdf,
            "converted_at": datetime.datetime.now(),
        },
        {
            "converted_from": jpg,
            "converted_to": pdf,
            "converted_at": datetime.datetime.now(),
        },
        {
            "converted_from": jpg,
            "converted_to": pdf,
            "converted_at": datetime.datetime.now(),
        },
    ]


@pytest.fixture
def converted_dict(get_uuid):
    jpg = model.JPG(code=get_uuid, src_path="fake.jpg")
    pdf = model.PDF(code=get_uuid, dest_path="fake.pdf")

    dict_ = {
        "converted_from": jpg,
        "converted_to": pdf,
        "converted_at": datetime.datetime.now(),
    }
    return [model.Converted.from_dict(dict_)]
