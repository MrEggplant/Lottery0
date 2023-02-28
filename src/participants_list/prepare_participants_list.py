from src.participants_list.participants import Participant
import csv
import json
from os.path import dirname
from pathlib import Path


def prepare_participants_list(participants_file):
    current_dir = dirname(__file__)
    participants_file = Path(current_dir).parent.joinpath(
        'data/participants/'+participants_file)
    participants_list = []

    if participants_file.suffix == '.csv':
        with open(participants_file, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            participants_list = get_data_to_list(reader)
    elif participants_file.suffix == '.json':
        with open(participants_file, 'r') as json_file:
            reader = json.load(json_file)
            participants_list = get_data_to_list(reader)
    else:
        print("Wrong file extension or file is not existed.")
        pass
    return participants_list


def get_data_to_list(reader):
    lottery_competitors = []
    for index, row in enumerate(reader):
        lottery_competitors.append(
            Participant(name=row['first_name'],
                        surname=row['last_name']
                        )
        )
        try:
            lottery_competitors[index].weight = row['weight']
        except KeyError:
            lottery_competitors[index].weight = 1
    return lottery_competitors
