import json
from src.domain import model
from src.serializers import model as serializer


def test_serialize_pdf(get_uuid):
    pdf = model.PDF(code=get_uuid, destination_path="random.pdf")
    json_obj = f"""
        {{
            "code": "{get_uuid}",
            "destination_path": "random.pdf",
            "extension": "{pdf.extension}"
        }}
    """
    json_pdf = json.dumps(pdf, cls=serializer.PDFSerializer)
    assert json.loads(json_pdf) == json.loads(json_obj)


def test_serialize_jpg(get_uuid):
    jpg = model.JPG(code=get_uuid, src_path="random.jpg")
    expected_json = f"""
        {{
            "code": "{get_uuid}",
            "src_path": "random.jpg",
            "extensions": "{list(jpg.extensions)}"
        }}
    """
    json_jpg = json.dumps(jpg, cls=serializer.JPGSerializer)
    assert json.loads(json_jpg) == json.loads(expected_json)
