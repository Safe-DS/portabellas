from typing import Any

import pytest

from portabellas import Column
from portabellas.exceptions import IndexOutOfBoundsError


@pytest.mark.parametrize(
    ("index", "expected"),
    [
        pytest.param(0, 0, id="first item (positive index)"),
        pytest.param(1, 1, id="last item (positive index)"),
        pytest.param(-2, 0, id="first item (negative index)"),
        pytest.param(-1, 1, id="last item (negative index)"),
    ],
)
def test_should_get_item_at_index(index: int, expected: Any) -> None:
    assert Column("col1", [0, 1]).get_value(index) == expected


@pytest.mark.parametrize(
    "index",
    [
        pytest.param(-3, id="too low"),
        pytest.param(2, id="too high"),
    ],
)
def test_should_raise_if_index_is_out_of_bounds(index: int) -> None:
    column = Column("col1", [0, 1])
    with pytest.raises(IndexOutOfBoundsError):
        column.get_value(index)
