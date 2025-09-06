from typing import Any

import pytest

from portabellas import Column


@pytest.mark.parametrize(
    ("column", "value", "expected"),
    [
        pytest.param(
            Column("col1", []),
            1,
            False,
            id="empty",
        ),
        pytest.param(
            Column("col1", [1]),
            1,
            True,
            id="value exists",
        ),
        pytest.param(
            Column("col1", [1]),
            2,
            False,
            id="value does not exist",
        ),
        pytest.param(
            Column("col1", [1]),
            "1",
            False,
            id="different type",
        ),
    ],
)
def test_should_check_whether_the_value_exists(column: Column, value: Any, expected: bool) -> None:
    assert (value in column) == expected
