from dataclasses import dataclass, field, asdict
from src.domain.validator import is_jpeg, is_pdf
import uuid


@dataclass
class JPG:
    code: uuid.UUID
    src_path: str
    extensions: tuple[str, str] = field(init=False, default=(".jpg", ".jpeg"))

    @classmethod
    def from_dict(cls, dict_):
        return cls(**dict_)

    def to_dict(self):
        return asdict(self)


@dataclass
class PDF:
    code: uuid.UUID
    destination_path: str
    extension: str = field(init=False, default=(".pdf"))


@is_jpeg
def allocate_jpeg(code: uuid.UUID, src_path: str) -> JPG:
    return JPG(code=code, src_path=src_path)


@is_pdf
def allocate_pdf(code: uuid.UUID, destination_path: str) -> PDF:
    return PDF(code=code, destination_path=destination_path)
