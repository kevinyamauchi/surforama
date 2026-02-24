from .app import QtSurforama

try:
    from surforama._version import __version__
except ImportError:
    __version__ = "unknown"

__all__ = ("QtSurforama",)
