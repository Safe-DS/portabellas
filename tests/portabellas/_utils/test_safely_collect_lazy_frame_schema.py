import polars as pl
import pytest

from portabellas._utils import safely_collect_lazy_frame_schema
from portabellas.exceptions import LazyComputationError


def test_should_raise_custom_error() -> None:
    frame = pl.LazyFrame().select("a")
    with pytest.raises(LazyComputationError):
        safely_collect_lazy_frame_schema(frame)
