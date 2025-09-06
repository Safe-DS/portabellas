from __future__ import annotations

from typing import TYPE_CHECKING

import polars as pl

from portabellas._utils import safely_collect_lazy_frame
from portabellas._validation import check_row_counts_are_equal
from portabellas.io import TableReader, TableWriter
from portabellas.plotting import TablePlotter

if TYPE_CHECKING:
    from collections.abc import Mapping, Sequence


class Table:
    """
    A two-dimensional collection of data. It can either be seen as a list of rows or as a list of columns.

    Parameters
    ----------
    data:
        The data of the table.

    Raises
    ------
    LengthMismatchError
        If columns have different lengths.

    Examples
    --------
    >>> from portabellas import Table
    >>> Table({"a": [1, 2, 3], "b": [4, 5, 6]})
    +-----+-----+
    |   a |   b |
    | --- | --- |
    | i64 | i64 |
    +===========+
    |   1 |   4 |
    |   2 |   5 |
    |   3 |   6 |
    +-----+-----+
    """

    # ------------------------------------------------------------------------------------------------------------------
    # Import
    # ------------------------------------------------------------------------------------------------------------------

    read: TableReader = TableReader()
    """Create a new table by reading from various sources."""
    # TODO: add examples  # noqa: FIX002

    @staticmethod
    def _from_polars_data_frame(data: pl.DataFrame) -> Table:
        result = object.__new__(Table)
        result.__data_frame_cache = data
        result._lazy_frame = data.lazy()
        return result

    @staticmethod
    def _from_polars_lazy_frame(data: pl.LazyFrame) -> Table:
        result = object.__new__(Table)
        result.__data_frame_cache = None
        result._lazy_frame = data
        return result

    # ------------------------------------------------------------------------------------------------------------------
    # Dunder methods
    # ------------------------------------------------------------------------------------------------------------------

    def __init__(self, data: Mapping[str, Sequence[object]]) -> None:
        # Validation
        check_row_counts_are_equal(data)

        # Fields
        self.__data_frame_cache: pl.DataFrame | None = None  # Scramble the name to prevent access from outside
        self._lazy_frame: pl.LazyFrame = pl.LazyFrame(data, strict=False)

    # ------------------------------------------------------------------------------------------------------------------
    # Properties
    # ------------------------------------------------------------------------------------------------------------------

    @property
    def _data_frame(self) -> pl.DataFrame:
        if self.__data_frame_cache is None:
            self.__data_frame_cache = safely_collect_lazy_frame(self._lazy_frame)
            # Break chain of polars objects
            self._lazy_frame = self.__data_frame_cache.lazy()

        return self.__data_frame_cache

    @property
    def plot(self) -> TablePlotter:
        """Create interactive plots of this table."""
        # TODO: add examples  # noqa: FIX002
        return TablePlotter(self)

    @property
    def write(self) -> TableWriter:
        """Write this table to various targets."""
        # TODO: add examples  # noqa: FIX002
        return TableWriter(self)
