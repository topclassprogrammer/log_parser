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
