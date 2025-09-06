import pytest

from portabellas import Table


@pytest.mark.parametrize(
    ("table", "expected"),
    [
        pytest.param(Table({}), 0, id="empty"),
        pytest.param(Table({"col1": []}), 0, id="no rows"),
        pytest.param(Table({"col1": [1, 2], "col2": [3, 4]}), 2, id="non-empty"),
    ],
)
def test_should_return_number_of_rows(table: Table, expected: int) -> None:
    assert table.row_count == expected
