import unittest

from bonuses import app


class BonusesApiTestCase(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
