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


def test_get_column_count(column_name: str, dict_lines_list: list[dict]):
    list_ = get_column_count(column_name, dict_lines_list)
    assert isinstance(list_, list)
    assert isinstance(list_[0]["total"], int)


def test_get_avg_response_time(dict_lines_list: list[dict],
                               url_count_list: list[dict]):
    list_ = get_avg_response_time(dict_lines_list, url_count_list)
    assert isinstance(list_, list)
    assert not hasattr(list_[0], "sum_response_time")
    assert isinstance(list_[0]["avg_response_time"], float)


def test_get_dates(date: str, dict_lines_list: dict[list]):
    list_ = get_dates(date, dict_lines_list)
    assert isinstance(list_, list)
    assert isinstance(list_[0]["@timestamp"], str)
    r = re.match(r"\d{4}-\d{2}-\d{2}", date)
    try:
        r = r[0]
        assert True
    except TypeError:
        assert False
