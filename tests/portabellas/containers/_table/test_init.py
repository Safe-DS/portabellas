import pytest

from portabellas import Table
from portabellas.exceptions import LengthMismatchError


def test_should_raise_if_row_counts_differ() -> None:
    with pytest.raises(LengthMismatchError):
        Table({"a": [1, 2], "b": [3]})
