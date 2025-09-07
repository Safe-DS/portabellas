import pytest

from portabellas import Column
from portabellas.typing import DataType


@pytest.mark.parametrize(
    ("column", "expected"),
    [
        pytest.param(Column("col1", [1]), DataType.Int64(), id="int"),
        pytest.param(Column("col1", ["a"]), DataType.String(), id="string"),
    ],
)
def test_should_return_type(column: Column, expected: DataType) -> None:
    assert column.type == expected
