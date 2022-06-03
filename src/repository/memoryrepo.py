from src.domain.model import Converted


class MemoryRepo:
    def __init__(self, data):
        self.data = data

    def list(self):
        return [Converted.from_dict(dict_) for dict_ in self.data]
