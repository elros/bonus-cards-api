import os
import unittest

os.environ['BONUSES_API_SETTINGS'] = os.path.join(os.path.dirname(__file__), 'settings.py')

from bonuses.app import app


class BonusesApiTestCase(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_client_login(self):
        pass


if __name__ == '__main__':
    unittest.main()
