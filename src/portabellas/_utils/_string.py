from __future__ import annotations

from difflib import get_close_matches
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable


def get_similar_strings(given_string: str, valid_strings: Iterable[str]) -> list[str]:
    close_matches = get_close_matches(given_string, valid_strings, n=3)

    if close_matches and close_matches[0] == given_string:
        return close_matches[:1]
    return close_matches
