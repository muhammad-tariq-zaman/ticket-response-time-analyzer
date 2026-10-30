import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import response_hours


class TestResponseTime(unittest.TestCase):
    def test_two_hours(self):
        self.assertAlmostEqual(response_hours("2026-10-28T09:00:00", "2026-10-28T11:00:00"), 2.0)

    def test_half_hour(self):
        self.assertAlmostEqual(response_hours("2026-10-28T09:00:00", "2026-10-28T09:30:00"), 0.5)
