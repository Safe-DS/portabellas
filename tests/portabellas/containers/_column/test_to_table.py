import pytest

from portabellas import Column, Table
from tests.helpers import assert_tables_are_equal


@pytest.mark.parametrize(
    ("column", "expected"),
    [
        pytest.param(
            Column("col1", []),
            Table({"col1": []}),
            id="empty",
        ),
        pytest.param(
            Column("col1", [1, 2, 3]),
            Table({"col1": [1, 2, 3]}),
            id="non-empty",
        ),
    ],
)
def test_should_return_table_with_this_column(column: Column, expected: Table) -> None:
    actual = column.to_table()
    assert_tables_are_equal(actual, expected)
