from __future__ import annotations

from collections.abc import Iterator, Sequence
from typing import TYPE_CHECKING

from portabellas._utils import safely_collect_lazy_frame

if TYPE_CHECKING:
    from portabellas import Table

import polars as pl

from portabellas.plotting import ColumnPlotter


class Column[T]:
    """
    A named, one-dimensional collection of homogeneous values.

    Parameters
    ----------
    name:
        The name of the column.
    data:
        The data of the column.

    Examples
    --------
    >>> from portabellas import Column
    >>> Column("a", [1, 2, 3])
    +-----+
    |   a |
    | --- |
    | i64 |
    +=====+
    |   1 |
    |   2 |
    |   3 |
    +-----+
    """

    # ------------------------------------------------------------------------------------------------------------------
    # Import
    # ------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def _from_polars_series(data: pl.Series) -> Column:
        result = object.__new__(Column)
        result._name = data.name
        result.__series_cache = data
        result._lazy_frame = data.to_frame().lazy()
        return result

    @staticmethod
    def _from_polars_lazy_frame(name: str, data: pl.LazyFrame) -> Column:
        result = object.__new__(Column)
        result._name = name
        result.__series_cache = None
        result._lazy_frame = data.select(name)
        return result

    # ------------------------------------------------------------------------------------------------------------------
    # Dunder methods
    # ------------------------------------------------------------------------------------------------------------------

    def __init__(self, name: str, data: Sequence[T]) -> None:
        # Fields
        self._name: str = name
        self.__series_cache: pl.Series | None = pl.Series(name, data, strict=False)
        self._lazy_frame: pl.LazyFrame = self.__series_cache.to_frame().lazy()


    def __iter__(self) -> Iterator[T]:
        return self._series.__iter__()


    # ------------------------------------------------------------------------------------------------------------------
    # Properties
    # ------------------------------------------------------------------------------------------------------------------

    @property
    def _series(self) -> pl.Series:
        if self.__series_cache is None:
            self.__series_cache = safely_collect_lazy_frame(self._lazy_frame).to_series()
            # Break chain of polars objects
            self._lazy_frame = self.__series_cache.to_frame().lazy()

        return self.__series_cache

    @property
    def name(self) -> str:
        """
        The name of the column.

        Examples
        --------
        >>> from portabellas import Column
        >>> column = Column("a", [1, 2, 3])
        >>> column.name
        'a'
        """
        return self._name

    @property
    def row_count(self) -> int:
        """
        The number of rows.

        **Notes:**

        - This operation loads the full data into memory, which can be expensive.

        Examples
        --------
        >>> from portabellas import Column
        >>> column = Column("a", [1, 2, 3])
        >>> column.row_count
        3
        """
        return self._series.len()

    @property
    def plot(self) -> ColumnPlotter:
        """Create interactive plots of this column."""
        # TODO: examples # noqa: FIX002
        return ColumnPlotter(self)
