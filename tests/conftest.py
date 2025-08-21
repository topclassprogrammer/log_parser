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
