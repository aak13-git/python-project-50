import argparse

from gendiff.scripts.read_file import read_file
from gendiff.scripts.stylish import stylish


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', type=str, help='путь к первому файлу')
    parser.add_argument('second_file', type=str, help='путь ко второму файлу')
    parser.add_argument(
        '-f', '--format',
        default='stylish',
        help='set format of output'
    )

    args = parser.parse_args()
    diff_result = generate_diff(args.first_file, args.second_file)
    return diff_result


def diff(file_1, file_2):
    node = {}
    union_keys = sorted(set(file_1.keys()) | set(file_2.keys()))
    for key in union_keys:
        val1 = file_1.get(key)
        val2 = file_2.get(key)
        if isinstance(val1, dict) and isinstance(val2, dict):
            node[key] = {
                'status': 'nested',
                'children': diff(val1, val2)
            }
        elif val1 == val2:
            node[key] = {'status': 'same', 'value': val1}
        elif key in file_1 and key in file_2:
            node[key] = {
                'status': 'updated',
                'old_value': val1,
                'new_value': val2
            }
        elif key in file_1:
            node[key] = {'status': 'removed', 'value': val1}
        else:
            node[key] = {'status': 'added', 'value': val2}
    return node


def generate_diff(path_1: str, path_2: str, format_name='stylish'):
    file_1 = read_file(path_1)
    file_2 = read_file(path_2)
    gen_diff = diff(file_1, file_2)
    return '{\n' + '\n'.join(stylish(gen_diff)) + '\n}'


if __name__ == '__main__':
    main()
