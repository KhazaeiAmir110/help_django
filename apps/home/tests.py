from django.test import SimpleTestCase


class TestFirst(SimpleTestCase):
    def test_fals(self):
        self.assertFalse(1 == 2)

    def test_true(self):
        self.assertTrue(1 == 1)
