from masonite.testing import TestCase


class TestUnit(TestCase):
    
    transactions = True
    sqlite = False

    def test_example_assertion(self):
        self.assertTrue(True)
