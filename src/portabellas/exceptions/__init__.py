class PortabellasError(Exception):
    """Base class for all exceptions defined by portabellas."""


class LengthMismatchError(PortabellasError, ValueError):
    """Raised when objects have different lengths."""


__all__ = ["LengthMismatchError", "PortabellasError"]
