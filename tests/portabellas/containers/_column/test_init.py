import pytest
from pytest import param

from portabellas import Column


def test_should_store_the_name() -> None:
    column = Column("col1", [])
    assert column.name == "col1"


@pytest.mark.parametrize(
    ("column", "expected"),
    [
        param(Column("col1", []), [], id="empty"),
        param(Column("col1", [1]), [1], id="non-empty (inferred type)"),
        # TODO
        # param(Column("col1", [1], type=ColumnType.string()), ["1"], id="non-empty (manifest type)"),
    ],
)
def test_should_store_the_data(column: Column, expected: list) -> None:
    assert list(column) == expected


# TODO
# @pytest.mark.parametrize(
#     ("column", "expected"),
#     [
#         param(Column("col1", []), ColumnType.null(), id="empty"),
#         param(Column("col1", [1]), ColumnType.int64(), id="non-empty (inferred type)"),
#         param(Column("col1", [1], type=ColumnType.string()), ColumnType.string(), id="non-empty (manifest type)"),
#     ],
# )
# def test_should_have_correct_type(column: Column, expected: ColumnType) -> None:
#     assert column.type == expected
