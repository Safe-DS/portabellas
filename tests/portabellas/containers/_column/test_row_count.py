import pytest

from portabellas import Column


@pytest.mark.parametrize(
    ("column", "expected"),
    [
        pytest.param(
            Column("col1", []),
            0,
            id="empty",
        ),
        pytest.param(
            Column("col1", [0]),
            1,
            id="non-empty",
        ),
    ],
)
def test_should_return_the_number_of_rows(column: Column, expected: int) -> None:
    assert column.row_count == expected
