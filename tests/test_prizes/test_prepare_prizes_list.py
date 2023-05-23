from os.path import dirname
from pathlib import Path
from src.prizes.prepare_prizes_list import prepare_prizes_list
from src.prizes.prizes import Prize
from unittest.mock import patch


def mock_prizes_path(file):
    current_dir = dirname(file)
    current_dir = Path(current_dir).parent.parent.joinpath('src/tests')
    return current_dir


class TestPreparePrizesList:
    @patch('src.prizes.prepare_prizes_list.dirname', mock_prizes_path)
    def test_prepare_prizes_list_no_template(self):
        results = prepare_prizes_list(None)
        prize = Prize(name='prize_name', amount='amount')
        assert type(results) is list
        assert type(results[0]) == type(prize)
        assert results[0].amount == 1
        assert results[0].name == 'Annual Vim subscription'

    @patch('src.prizes.prepare_prizes_list.dirname', mock_prizes_path)
    def test_prepare_prizes_list_lottery_template(self):
        results = prepare_prizes_list('item_giveaway.json')
        prize = Prize(name='prize_name', amount='amount')
        assert type(results) is list
        assert type(results[0]) == type(prize)
