#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `fsdesign` package."""


import unittest
import os

from click.testing import CliRunner

from fsdesign import fsdesign
from fsdesign import cli

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

class TestFsdesign(unittest.TestCase):
    """Tests for `fsdesign` package."""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.factors_csv = os.path.join(THIS_DIR, 'data/factors.csv')
        self.text_template_file = os.path.join(THIS_DIR, 'data/template.txt')
        self.output_csv = os.path.join(THIS_DIR, 'data/output.csv')

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    @unittest.skip
    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'fsdesign.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output

    def test_fsdesign(self):
        factors = fsdesign.read_factors(self.factors_csv)
        with open(self.text_template_file) as f:
            text_template = f.read()
        fsexperiment = fsdesign.FSDesign(text_template, factors, size=6, duplicates=False)
        fsexperiment.to_csv(self.output_csv)


if __name__ == '__main__':
    unittest.main()
