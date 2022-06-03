import json
from typing import Any


class PDFSerializer(json.JSONEncoder):
    def default(self, object: Any) -> Any:
        try:
            return {
                "code": str(object.code),
                "destination_path": object.destination_path,
                "extension": object.extension,
            }
        except AttributeError:
            return super().default(object)


class JPGSerializer(json.JSONEncoder):
    def default(self, object: Any) -> Any:
        try:
            return {
                "code": str(object.code),
                "src_path": object.src_path,
                "extensions": f"{list(object.extensions)}",
            }
        except AttributeError:
            return super().default(object)
