from polars.testing import assert_frame_equal

from portabellas import Table


def assert_tables_are_equal(
    actual: Table,
    expected: Table,
    *,
    ignore_column_order: bool = False,
    ignore_row_order: bool = False,
    ignore_types: bool = False,
    ignore_float_imprecision: bool = True,
) -> None:
    """
    Assert that two tables are equal.

    Parameters
    ----------
    actual:
        The actual table.
    expected:
        The expected table.
    ignore_column_order:
        Ignore differences in column order.
    ignore_row_order:
        Ignore differences in row order.
    ignore_types:
        Ignore differences between types.
    ignore_float_imprecision:
        Ignore minor differences between floats.
    """
    assert_frame_equal(
        actual._data_frame,
        expected._data_frame,
        check_column_order=not ignore_column_order,
        check_row_order=not ignore_row_order,
        check_dtypes=not ignore_types,
        check_exact=not ignore_float_imprecision,
    )
