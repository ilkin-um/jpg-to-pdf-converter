import json
from src.domain import model
from src.serializers import model as model_serializer


def test_serialize_pdf(get_uuid):
    pdf = model.PDF(code=get_uuid, destination_path="random.pdf")
    json_obj = f"""
        {{
            "code": "{get_uuid}",
            "destination_path": "random.pdf",
            "extension": "{pdf.extension}"
        }}
    """
    json_pdf = json.dumps(pdf, cls=model_serializer.PDFJsonEncoder)
    assert json.loads(json_pdf) == json.loads(json_obj)
