import pytest

from portabellas import Column


@pytest.mark.parametrize(
    ("column", "expected"),
    [
        pytest.param(
            Column("col1", []),
            """

+------+
| col1 |
| ---  |
| null |
+======+
+------+

            """.strip(),
            id="empty",
        ),
        pytest.param(
            Column("col1", [0]),
            """

+------+
| col1 |
|  --- |
|  i64 |
+======+
|    0 |
+------+

            """.strip(),
            id="non-empty",
        ),
    ],
)
def test_should_return_a_string_representation(column: Column, expected: str) -> None:
    assert repr(column) == expected
