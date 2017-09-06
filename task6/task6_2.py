# Задание 6_2
# Вы должны на основе тестов написать исходную функцию:
# class TestFizzBuzz(unittest.TestCase):
#     def test_with_range(self):
#         self.assertEqual(main.fizzbuzz(range(1, 21)),
#                          [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8,
#                           'Fizz', 'Buzz', 11, 'Fizz', 13, 14,
#                           'FizzBuzz', 16, 17, 'Fizz', 19, 'Buzz'])
#
#     def test_normal(self):
#         self.assertEquals(main.fizzbuzz([1, 27, 45, 4, 7, 8, 9, 0]),
#                           [1, 'Fizz', 'FizzBuzz', 4, 7, 8, 'Fizz', 'FizzBuzz'])
#
#     def test_empty(self):
#         self.assertListEqual(main.fizzbuzz([]), [])

def fizzbuzz(var):    
    buf = []
    if var:
        for i in list(var):
            str = ''
            if i % 3 is 0:
                str += 'Fizz'
            if i % 5 is 0:
                str += 'Buzz'
            buf.append(str if str else i)
    return buf