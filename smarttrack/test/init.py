
import unittest
from flask import current_app
from app import create_app
class BasicTestCase(unittest.TestCase):
    def setup(self):
        