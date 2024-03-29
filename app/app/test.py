"""
Sample test cases


"""


from django.test import SimpleTestCase
from . import calc

"""test the calc module"""


class TestCase(SimpleTestCase):
    def test_add_number(self):
        a = 5
        b = 6
        c = calc.add(a, b)
        self.assertEqual(c, 11)

    def test_sub_number(self):
        a = 5
        b = 6
        c = calc.diff(a, b)
        self.assertEqual(c, 1)
