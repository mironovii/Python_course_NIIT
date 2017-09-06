# Тесты задания 6_2
import unittest, task6_2


class TestFizzBuzz(unittest.TestCase):
    def test_with_range(self):
        self.assertEqual(task6_2.fizzbuzz(range(1, 21)),
                         [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8,
                          'Fizz', 'Buzz', 11, 'Fizz', 13, 14,
                          'FizzBuzz', 16, 17, 'Fizz', 19, 'Buzz'])

    def test_normal(self):
        self.assertEquals(task6_2.fizzbuzz([1, 27, 45, 4, 7, 8, 9, 0]),
                          [1, 'Fizz', 'FizzBuzz', 4, 7, 8, 'Fizz', 'FizzBuzz'])

    def test_empty(self):
        self.assertListEqual(task6_2.fizzbuzz([]), [])
