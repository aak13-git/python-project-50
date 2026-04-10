import argparse

from gendiff.scripts.read_file import read_file


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


def generate_diff(path_1: str, path_2: str):
    file_1 = read_file(path_1)
    file_2 = read_file(path_2)
    all_keys = sorted(file_1.keys() | file_2.keys())
    result_lines = []

    for key in all_keys:
        in_first = key in file_1
        in_second = key in file_2

        if in_first and in_second:
            if file_1[key] == file_2[key]:
                result_lines.append(f"    {key}: {file_1[key]}")
            else:
                result_lines.append(f"  - {key}: {file_1[key]}")
                result_lines.append(f"  + {key}: {file_2[key]}")
        elif in_first:
            result_lines.append(f"  - {key}: {file_1[key]}")
        else:
            result_lines.append(f"  + {key}: {file_2[key]}")

    return "{\n" + "\n".join(result_lines) + "\n}"


if __name__ == '__main__':
    main()
