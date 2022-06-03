import datetime
import uuid
import json
from flask import Blueprint, Response

from src.domain import model
from src.repository.memoryrepo import MemoryRepo
from src.use_cases.converted_list import converted_list
from src.serializers.model import ConvertedJsonEncoder

blueprint = Blueprint("convert", __name__)


def _get_converted_list():
    jpg = model.JPG(code=uuid.uuid4(), src_path="random.jpg")
    pdf = model.PDF(code=uuid.uuid4(), destination_path="random.pdf")
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


@blueprint.route("/converteds", methods=["GET"])
def get_converted_list():
    repo = MemoryRepo(_get_converted_list())
    result = converted_list(repo)
    return Response(
        json.dumps(result, cls=ConvertedJsonEncoder),
        mimetype="application/json",
        status=200,
    )
