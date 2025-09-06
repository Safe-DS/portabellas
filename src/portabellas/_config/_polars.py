from __future__ import annotations

import polars as pl


def get_polars_config() -> pl.Config:
    return pl.Config(
        float_precision=5,
        tbl_cell_numeric_alignment="RIGHT",
        tbl_formatting="ASCII_FULL_CONDENSED",
        tbl_hide_dataframe_shape=True,
    )
