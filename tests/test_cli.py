"""Tests for CLI functionality."""

def test_cli_import():
    from vikrant_obl import cli
    assert cli is not None

def test_vobl_command():
    from vikrant_obl.cli import main
    assert main is not None
