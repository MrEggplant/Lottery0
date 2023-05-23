from src.participants_list.prepare_participants_list import prepare_participants_list
from src.participants_list.prepare_participants_list import Participant
from src.participants_list.prepare_participants_list import get_data_to_list
from os.path import dirname
from pathlib import Path
from unittest.mock import patch
import pytest
import csv
import json


def mock_participants_list(file):
    current_dir = dirname(file)
    current_dir = Path(current_dir).parent.parent.joinpath('src/tests')
    return current_dir


def prepare_files_for_reader(participants_file):
    current_dir = dirname(__file__)
    participants_file = Path(current_dir).parent.joinpath(
        'data/participants/' + participants_file)
    return participants_file


participant = Participant(name='Emil', surname='Test', weight='0')


class TestParticipantsList:
    @pytest.mark.parametrize(
        'participants_file', ('participants1.csv', 'participants2.csv', 'participants1.json', 'participants2.json')
    )
    @patch('src.participants_list.prepare_participants_list.dirname', mock_participants_list)
    def test_prepare_participants_list(self, participants_file):
        results = prepare_participants_list(participants_file)
        assert len(results) == 30
        assert type(results[0]) == type(participant)

    @pytest.mark.parametrize(
        'participants_file', ('participants1.csv', 'participants2.csv', 'participants1.json', 'participants2.json')
    )
    def test_get_data_to_list(self, participants_file):
        participants_file = prepare_files_for_reader(participants_file)
        if participants_file.suffix == '.csv':
            with open(participants_file, 'r') as csv_file:
                reader = csv.DictReader(csv_file)
                results = get_data_to_list(reader)
                assert len(results) == 30
                for competitor in results:
                    assert type(competitor) == type(participant)
                if participants_file.name == 'participants1':
                    for competitor in results:
                        assert competitor.weight == '1'

        elif participants_file.suffix == '.json':
            with open(participants_file, 'r') as json_file:
                reader = json.load(json_file)
                results = get_data_to_list(reader)
                assert len(results) == 30
                for competitor in results:
                    assert type(competitor) == type(participant)
                if participants_file.name == 'participants1':
                    for competitor in results:
                        assert competitor.weight == '1'
