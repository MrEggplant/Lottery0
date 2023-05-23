from unittest.mock import patch
from tempfile import TemporaryDirectory
from src.utils.save_results_to_file import save_and_show_lottery_results
from src.utils.save_results_to_file import make_path_for_results

winners_list_for_dump = [
    {'first_name': 'Emil', 'last_name': 'Abrams', 'prizes': 'Gold medal'},
    {'first_name': 'Jack', 'last_name': 'Leopard', 'prizes': 'Silver medal'},
    {'first_name': 'Adam', 'last_name': 'K2', 'prizes': 'Bronze medal'}
]


def create_test_directory():
    test_directory = TemporaryDirectory()
    return test_directory


class TestSaveAndShowResults:
    def test_save_and_show_lottery_results_no_dir_name(self):
        name_for_results_file = None
        lottery_results = save_and_show_lottery_results(winners_list_for_dump, name_for_results_file)
        assert lottery_results is None

    @patch('src.utils.save_results_to_file.dirname', lambda x: 'parent/test_dir')
    def test_make_path_for_results(self):
        result = make_path_for_results().as_posix()
        assert result == 'parent/data/results'
