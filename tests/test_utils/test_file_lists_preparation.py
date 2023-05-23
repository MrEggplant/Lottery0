from src.utils.file_lists_preparation import file_list_preparation
from unittest.mock import patch
import pytest


class TestFileListPreparation:
    @pytest.mark.parametrize('file_type', ('participants', 'lottery_templates'))
    def test_file_list_preparation(self, file_type):
        results = file_list_preparation(file_type)
        if file_type == 'participants':
            assert len(results) == 4
        if file_type == 'lottery_template':
            assert len(results) == 2

    @patch('src.utils.file_lists_preparation.print', lambda x: 'wrong_type')
    def test_file_list_preparation_wrong_file_type(self):
        results = file_list_preparation(file_type='wrong_type')
        assert results is None
