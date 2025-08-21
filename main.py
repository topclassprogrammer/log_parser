import argparse
import json

from tabulate import tabulate


def get_parsed_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", nargs="*")
    parser.add_argument("--report")
    parser.add_argument("--date")
    args = parser.parse_args()
    return args


def get_dict_lines_list(args: argparse.Namespace) -> list[dict]:
    dict_lines_list = []
    for filename in args.file:
        try:
            with open(filename, "r", encoding="utf-8") as f:
                for line in f.readlines():
                    dict_line = json.loads(line)
                    dict_lines_list.append(dict_line)
        except FileNotFoundError:
            print(f"File {filename.strip(".\\")} not found " 
                  f"in the current directory.")
    return dict_lines_list
