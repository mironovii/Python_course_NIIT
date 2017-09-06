# Тесты задания 6_1
import unittest, task6_1
from task6_1 import to_roman


class TestToRoman(unittest.TestCase):
    def test_1(self):
        self.assertEqual(to_roman(1), 'I')
        self.assertEqual(to_roman(34), 'XXXIV')
        self.assertEqual(to_roman(99), 'XCIX')
        self.assertEqual(to_roman(654), 'DCLIV')
        self.assertEqual(to_roman(962), 'CMLXII')
        self.assertEqual(to_roman(3833), 'MMMDCCCXXXIII')
        self.assertEqual(to_roman(4900), 'MMMMCM')

    def test_2(self):
        with self.assertRaises(task6_1.NonValidInput):
            to_roman('str')
        with self.assertRaises(task6_1.NonValidInput):
            to_roman(2.0)
        with self.assertRaises(task6_1.NonValidInput):
            to_roman(-12)
        with self.assertRaises(task6_1.NonValidInput):
            to_roman(7584)
