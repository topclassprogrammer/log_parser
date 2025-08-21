import argparse
import pytest


@pytest.fixture
def args() -> argparse.Namespace:
    argparser = argparse.Namespace(
        file=["example1.log"], report="average", date="2025-06-22")
    return argparser


@pytest.fixture
def column_name() -> str:
    return "url"


@pytest.fixture
def dict_lines_list() -> list[dict]:
    return [
        {
            "@timestamp": "2025-06-22T13:57:32+00:00",
            "status": 200,
            "url": "/api/context/...",
            "request_method": "GET",
            "response_time": 0.024,
            "http_user_agent": "...",
        }
    ]


@pytest.fixture
def url_count_list() -> list[dict]:
    return [{"url": "/api/context/...", "total": 21}]


@pytest.fixture
def date() -> str:
    return "2025-06-22"


@pytest.fixture
def filename() -> str:
    return "average"
