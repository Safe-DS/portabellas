import pytest

from portabellas import Column
from pytest import param

@pytest.mark.parametrize(
    ("column", "expected"),
    [
        param(Column("col1", []), [], id="empty",),
        param(Column("col1", [0]), [0], id="non-empty",),
    ],
)
def test_should_iterate_over_the_data(column: Column, expected: list) -> None:
    assert list(column) == expected
