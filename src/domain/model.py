from dataclasses import dataclass, field
from src.domain.validator import is_jpeg, is_pdf


@dataclass
class JPG:
    src_path: str
    extensions: tuple[str, str] = field(init=False, default=(".jpg", ".jpeg"))


@dataclass
class PDF:
    destination_path: str
    extension: str = field(init=False, default=(".pdf"))


@is_jpeg
def allocate_jpeg(src_path: str) -> JPG:
    return JPG(src_path=src_path)


@is_pdf
def allocate_pdf(destination_path: str) -> PDF:
    return PDF(destination_path=destination_path)
