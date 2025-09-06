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
    assert Column("a", [0, 1])[index] == expected


@pytest.mark.parametrize(
    ("index", "expected"),
    [
        pytest.param(slice(0, 0), [], id="empty"),
        pytest.param(slice(0, 1), [0], id="first item"),
        pytest.param(slice(2, 3), [2], id="last item"),
        pytest.param(slice(0, 3), [0, 1, 2], id="all items"),
        pytest.param(slice(0, 3, 2), [0, 2], id="every other item"),
        pytest.param(slice(-1, None), [2], id="negative start index"),
        pytest.param(slice(None, -1), [0, 1], id="negative end index"),
        pytest.param(slice(None, None, -1), [2, 1, 0], id="negative step"),
        pytest.param(slice(100, None), [], id="high start index (step=1)"),
        pytest.param(slice(100, None, -1), [2, 1, 0], id="high start index (step=-1)"),
        pytest.param(slice(None, 100), [0, 1, 2], id="high end index (step=1)"),
        pytest.param(slice(None, 100, -1), [], id="high end index (step=-1)"),
        pytest.param(slice(-100, None), [0, 1, 2], id="low start index (step=1)"),
        pytest.param(slice(-100, None, -1), [], id="low start index (step=-1)"),
        pytest.param(slice(None, -100), [], id="low end index (step=1)"),
        pytest.param(slice(None, -100, -1), [2, 1, 0], id="low end index (step=-1)"),
    ],
)
def test_should_get_items_in_slice(index: slice, expected: list) -> None:
    assert list(Column("col1", [0, 1, 2])[index]) == expected


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
