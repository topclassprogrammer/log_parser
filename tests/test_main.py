import argparse
import json
import re

from main import (get_avg_response_time, get_column_count, get_dates,
                  get_dict_lines_list, main, save_report)


def test_get_dict_lines_list(args: argparse.Namespace):
    dict_lines_list = get_dict_lines_list(args)
    assert isinstance(dict_lines_list, list)
    filename = getattr(args, "file")
    with open(filename[0]) as f:
        for line in f.readlines():
            dict_line = json.loads(line)
            assert isinstance(dict_line, dict)
