#!/usr/bin/python3
import unittest
"""A class for testing"""


class TestSomething(unittest.TestCase):
    """Test something"""
    def test_smtn(self):
        self.assertEqual(2, 3)
