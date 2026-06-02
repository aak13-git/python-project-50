import json
from pathlib import Path

import yaml


def read_file(path: str):
    permission = Path(path).suffix
    if permission == '.json':
        with open(path) as file:
            parsed_file = json.load(file)
        return parsed_file

    elif permission in ('.yaml', '.yml'):
        with open(path) as file:
            parsed_file = yaml.safe_load(file)
        return parsed_file

    else:
        with open(path, encoding='utf-8') as file:
            return file.read()


if __name__ == '__main__':

    path = str(input('Введите путь до файла: '))
    read_file(path)
