import os
import unittest

os.environ['BONUSES_API_SETTINGS'] = os.path.join(os.path.dirname(__file__), 'settings.py')

from bonuses.app import bonuses_app


class BonusesApiTestCase(unittest.TestCase):

    def setUp(self):
        bonuses_app.testing = True
        self.app = bonuses_app.test_client()

    def test_client_login(self):
        pass


if __name__ == '__main__':
    unittest.main()
