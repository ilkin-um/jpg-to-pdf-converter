def is_jpeg(src: str) -> bool:
    return src.endswith(".jpg") or src.endswith(".jpeg")


def is_pdf(src: str) -> bool:
    return src.endswith(".pdf")
