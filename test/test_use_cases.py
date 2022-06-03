from unittest import mock

from src.use_cases.converted_list import converted_list


def test_converted_list(converted_data):
    repo = mock.Mock()
    repo.list.return_value = converted_data
    result = converted_list(repo)
    repo.list.assert_called_with()
    assert result == converted_data
