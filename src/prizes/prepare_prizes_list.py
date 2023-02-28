import json
from pathlib import Path
from os.path import dirname
from src.utils.file_lists_preparation import file_list_preparation
from src.prizes.prizes import Prize


def prepare_prizes_list(lottery_template):
    prizes = []
    if lottery_template is None:
        file_list = file_list_preparation('lottery_templates')
        lottery_template = file_list[0]

    current_dir = dirname(__file__)
    lottery_template = Path(current_dir).parent.joinpath('data/lottery_templates/'+lottery_template)
    with open(lottery_template, 'r') as json_file:
        reader = json.load(json_file)
        for row in reader['prizes']:
            while row['amount'] >= 1:
                prizes.append(
                    Prize(name=row['name'], amount=1)
                )
                row['amount'] = row['amount'] - 1
    return prizes
