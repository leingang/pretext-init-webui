import unittest

import pretext_init


class Pretext_initTestCase(unittest.TestCase):

    def setUp(self):
        self.app = pretext_init.app.test_client()

    def test_index(self):
        rv = self.app.get('/')
        self.assertIn('Welcome to PreTeXt Init', rv.data.decode())


if __name__ == '__main__':
    unittest.main()
