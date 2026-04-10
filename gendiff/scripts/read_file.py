import json


def read_file(path: str) -> dict:
    with open(path) as file:
        parsed_file = json.load(file)

    return parsed_file


if __name__ == '__main__':

    path = str(input('Введите путь до файла: '))
    read_file(path)
