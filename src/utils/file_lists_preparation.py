from os.path import dirname
from pathlib import Path

FILE_TYPES = {'participants': 'participants*', 'lottery_templates': '*'}


def file_list_preparation(file_type):
    current_dir = dirname(__file__)
    file_names = []
    if file_type in FILE_TYPES:
        data_dir_path = Path(current_dir).parent.joinpath('data/' + file_type)
        paths_list = list(data_dir_path.glob(FILE_TYPES[file_type]))
        for file in paths_list:
            file_names.append(file.name)
        return file_names
    else:
        print("Wrong file type.")
