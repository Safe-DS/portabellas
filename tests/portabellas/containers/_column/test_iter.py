from typing import Any

import pytest

from portabellas import Column


@pytest.mark.parametrize(
    ("column", "expected"),
    [
        pytest.param(
            Column("col1", []),
            [],
            id="empty",
        ),
        pytest.param(
            Column("col1", [0]),
            [0],
            id="non-empty",
        ),
    ],
)
def test_should_iterate_over_the_data(column: Column, expected: list[Any]) -> None:
    assert list(column) == expected
