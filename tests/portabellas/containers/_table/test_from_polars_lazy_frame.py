from typing import Any

import polars as pl
import pytest
from pytest import param

from portabellas import Table
from tests.helpers import assert_tables_are_equal


@pytest.mark.parametrize(
    "data",
    [
        param({}, id="empty"),
        param({"col1": []}, id="no rows"),
        param({"col1": [1, 2], "col2": [3, 4]}, id="non-empty"),
    ],
)
def test_should_create_table(data: dict[str, list[Any]]) -> None:
    actual = Table._from_polars_lazy_frame(pl.LazyFrame(data))
    expected = Table(data)
    assert_tables_are_equal(actual, expected)
