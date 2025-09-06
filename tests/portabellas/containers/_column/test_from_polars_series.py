import polars as pl
import pytest

from portabellas import Column


def test_should_store_the_name() -> None:
    series = pl.Series("col1", [])
    assert Column._from_polars_series(series).name == "col1"


@pytest.mark.parametrize(
    ("series", "expected"),
    [
        pytest.param(
            pl.Series([]),
            [],
            id="empty",
        ),
        pytest.param(
            pl.Series([True]),
            [True],
            id="non-empty",
        ),
    ],
)
def test_should_store_the_data(series: pl.Series, expected: list) -> None:
    assert list(Column._from_polars_series(series)) == expected
