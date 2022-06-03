from src.domain.model import Converted
from src.repository.memoryrepo import MemoryRepo


def test_repository_list(converted_dicts):
    repo = MemoryRepo(converted_dicts)
    converted_list = [Converted.from_dict(dict_) for dict_ in converted_dicts]
    assert repo.list() == converted_list
