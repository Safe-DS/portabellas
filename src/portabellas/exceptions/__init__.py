class PortabellasError(Exception):
    """Base class for all exceptions defined by portabellas."""


class LazyComputationError(PortabellasError, RuntimeError):
    """Raised when a lazy computation fails."""


class LengthMismatchError(PortabellasError, ValueError):
    """Raised when objects have different lengths."""


__all__ = ["LazyComputationError", "LengthMismatchError", "PortabellasError"]
