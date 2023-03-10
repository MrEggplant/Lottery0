from pathlib import Path
from os.path import dirname
import os
import json


def save_and_show_lottery_results(winners_list_for_dump, name_for_results_file):
    if name_for_results_file is None:
        pass
    else:
        current_dir = dirname(__file__)
        data_dir_path = Path(current_dir).parent.joinpath('data/results')

        if not data_dir_path.exists():
            data_dir_path.mkdir()

        file_name = f"{name_for_results_file}.{'json'}"
        results_file = os.path.join(data_dir_path, file_name)

        with open(results_file, 'a') as json_file:
            json.dump(winners_list_for_dump, json_file)
