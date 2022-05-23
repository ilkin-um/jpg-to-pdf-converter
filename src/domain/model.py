from dataclasses import dataclass, field
from src.domain.validators import is_jpeg, is_pdf


@dataclass
class JPG:
    src_path: str
    extensions: tuple[str, str] = field(init=False, default=(".jpg", ".jpeg"))


@dataclass
class PDF:
    destination_path: str
    extension: str = field(init=False, default=(".pdf"))


def allocate_jpeg(src_path: str) -> JPG:
    if is_jpeg(src_path):
        return JPG(src_path=src_path)


def allocate_pdf(destination_path: str) -> PDF:
    if is_pdf(destination_path):
        return PDF(destination_path=destination_path)
