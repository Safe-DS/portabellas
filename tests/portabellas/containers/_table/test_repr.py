import pytest
from pytest import param

from portabellas import Table


@pytest.mark.parametrize(
    ("table", "expected"),
    [
        param(
            Table({}),
            """

++
++
++

            """.strip(),
            id="empty",
        ),
        param(
            Table({"col1": [], "col2": []}),
            """

+------+------+
| col1 | col2 |
| ---  | ---  |
| null | null |
+=============+
+------+------+

            """.strip(),
            id="no rows",
        ),
        param(
            Table({"col1": [1, 2], "col2": [3, 4]}),
            """

+------+------+
| col1 | col2 |
|  --- |  --- |
|  i64 |  i64 |
+=============+
|    1 |    3 |
|    2 |    4 |
+------+------+

            """.strip(),
            id="with data",
        ),
    ],
)
def test_should_return_a_string_representation(table: Table, expected: str) -> None:
    assert repr(table) == expected
