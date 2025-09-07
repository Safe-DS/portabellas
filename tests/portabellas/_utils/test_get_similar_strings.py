import pytest

from portabellas._utils import get_similar_strings


@pytest.mark.parametrize(
    ("string", "valid_strings", "expected"),
    [
        pytest.param(
            "column1",
            [],
            [],
            id="empty",
        ),
        pytest.param(
            "column1",
            ["column1", "column2"],
            ["column1"],
            id="exact match",
        ),
        pytest.param(
            "dissimilar",
            ["column1", "column2", "column3"],
            [],
            id="no similar",
        ),
        pytest.param(
            "cilumn1",
            ["column1", "x", "y"],
            ["column1"],
            id="one similar",
        ),
        pytest.param(
            "cilumn1",
            ["column1", "column2", "y"],
            ["column1", "column2"],
            id="multiple similar",
        ),
    ],
)
def test_should_get_similar_strings(string: str, valid_strings: list[str], expected: list[str]) -> None:
    assert get_similar_strings(string, valid_strings) == expected
