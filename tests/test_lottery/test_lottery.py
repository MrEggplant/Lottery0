from src.participants_list.participants import Participant
from src.lottery.lottery import Lottery
from src.prizes.prizes import Prize
import pytest
from unittest.mock import patch


participants = [
    Participant('Emil', 'Test', '1'),
    Participant('Arek', 'Test', '2'),
    Participant('Manfred', 'Test', '3'),
]

prizes = [
    Prize('First_prize', '1'),
    Prize('Second_prize', '1'),
    Prize('Third_prize', '1')
]

lottery = Lottery(
    participants_list=participants,
    prizes_list=prizes
)


class TestLottery:
    @pytest.mark.parametrize(
        'number_of_winners', (1, 2, 3)
    )
    def test_run_lottery_winners_amount_and_type(self, number_of_winners):
        results = lottery.run_lottery(number_of_winners)
        assert len(results) == number_of_winners
        for result in results:
            assert type(result) == Participant

    def test_run_lottery(self):
        one_man_lottery = Lottery(
            participants_list=[Participant('Emil', 'Test', '1')],
            prizes_list=[Prize('First_prize', '1')]
        )
        results = one_man_lottery.run_lottery(1)
        assert results[0].name == 'Emil'
        assert results[0].surname == 'Test'
        assert results[0].weight == '1'
