from typing import Any

import pytest

from portabellas import Column


def test_should_store_the_name() -> None:
    column = Column("col1", [])
    assert column.name == "col1"


@pytest.mark.parametrize(
    ("column", "expected"),
    [
        pytest.param(Column("col1", []), [], id="empty"),
        pytest.param(Column("col1", [1]), [1], id="non-empty (inferred type)"),
    ],
)
def test_should_store_the_data(column: Column, expected: list[Any]) -> None:
    assert list(column) == expected
