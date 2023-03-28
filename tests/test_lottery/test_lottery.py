from tempfile import NamedTemporaryFile
from unittest.mock import patch

import pytest
from src.lottery.lottery import Lottery
from src.participants_list.participants import Participant


participants = [
    Participant('arek', 'x'),
    Participant('emil', 'y')
]

class TestLottery:

    # pytest fixture

    def test_run_lottery_no_weights(self):
        # arrange
        number_of_winners = 1

        prizes = ['boat', 'bike']
        lottery = Lottery(participants, prizes)

        # act
        result = lottery.run_lottery(number_of_winners)

        # assert
        assert len(result) == number_of_winners



    # @patch('src.lottery.lottery.random', random_mock)
    @pytest.mark.parametrize(
        'num_winners', (1, 2, 3, 0)
    )
    def test_run_lottery_no_weights_2(self, num_winners):
        prizes = ['boat', 'bike']
        lottery = Lottery(participants, prizes)

        # act
        result = lottery.run_lottery(num_winners)

        # assert
        assert len(result) == num_winners


    @pytest.mark.parametrize(
        'num_winners, another_arg', (
            (1, 'one'),
            (2, 'two'),
            (3, 'three')
        )
    )
    def test_run_lottery_no_weights_2(self, num_winners, another_arg):
        prizes = ['boat', 'bike']
        lottery = Lottery(participants, prizes)

        # act
        result = lottery.run_lottery(num_winners)

        # assert
        assert len(result) == num_winners
        print(another_arg)


    def test_x(self):
        temp_f = NamedTemporaryFile()

