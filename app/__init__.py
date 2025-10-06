"""Application package initializer.

Exposes __version__ sourced from pyproject.toml so tools and runtime code
can introspect the current package version. python-semantic-release will
update the version in pyproject and create tags; runtime code can read
this constant if needed.
"""

__all__ = ["__version__"]

__version__ = "0.1.0"
