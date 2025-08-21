import argparse
import json
import sys

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
            sys.exit()
    return dict_lines_list


def get_column_count(column_name: str, dict_lines_list: list[dict]) \
        -> list[dict] | None:
    if not column_name:
        return None
    dict_ = {}
    for x in dict_lines_list:
        try:
            if x[column_name] in dict_:
                dict_[x[column_name]] += 1
            else:
                dict_[x[column_name]] = 1
        except KeyError as e:
            print(f"Column {e} not found")
            sys.exit()
    list_ = [{column_name: k, "total": v} for k, v in dict_.items()]
    return list_


def get_avg_response_time(dict_lines_list: list[dict],
                          url_count_list: list[dict]) -> list[dict]:
    for i in dict_lines_list:
        time = i["response_time"]
        for indx, j in enumerate(url_count_list):
            if i["url"] == j["url"]:
                if url_count_list[indx].get("sum_response_time"):
                    url_count_list[indx]["sum_response_time"] += time
                else:
                    url_count_list[indx]["sum_response_time"] = time
    for el in url_count_list:
        el["avg_response_time"] = round(el["sum_response_time"] / el["total"], 3)
    for x in url_count_list:
        x.pop("sum_response_time")
    return url_count_list


def get_dates(date: str, dict_lines_list: list[dict]) -> list[dict] | None:
    if not date:
        return None
    dict_list = []
    for x in dict_lines_list:
        try:
            log_date = x["@timestamp"]
        except KeyError as e:
            print(f"Column {e} not found")
            sys.exit()
        if log_date.startswith(date):
            dict_list.append(x)
    return dict_list


def save_report(filename: str, dict_lines_list: list[dict]) -> None:
    if not filename:
        return None
    with open(filename, "w", encoding="utf-8") as f:
        f.write(tabulate(dict_lines_list, headers="keys", showindex=True))


def show_table(list_dicts: list[dict]) -> None:
    print(tabulate(list_dicts, headers="keys", showindex=True))


def main() -> None:
    args = get_parsed_args()
    dict_lines_list = get_dict_lines_list(args)
    url_count = get_column_count("url", dict_lines_list)
    user_agent_count = get_column_count("http_user_agent", dict_lines_list)
    avg_response_time = get_avg_response_time(dict_lines_list, url_count)
    dates = get_dates(args.date, dict_lines_list)
    show_table(avg_response_time)
    show_table(user_agent_count)
    show_table(dates)
    save_report(args.report, avg_response_time)


if __name__ == "__main__":
    main()
