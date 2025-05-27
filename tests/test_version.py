"""Unit tests for __version__.py."""

import montypy.meaning


def test_package_version():
    """Ensure the package version is defined and not set to the initial
    placeholder."""
    assert hasattr(montypy.meaning, "__version__")
    assert montypy.meaning.__version__ != "0.0.0"
