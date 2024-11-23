import unittest
from Solution import sum_two

class TestStrictDecorator(unittest.TestCase):
    def test_valid_arguments(self):
        """Тест с корректными аргументами"""
        self.assertEqual(sum_two(2, 3), 5)
        self.assertEqual(sum_two(-1, 1), 0)

    def test_invalid_argument_type(self):
        """Тест с некорректным типом аргумента"""
        with self.assertRaises(TypeError):
            sum_two(2, '3')  # Второй аргумент должен быть int

        with self.assertRaises(TypeError):
            sum_two('2', 3)  # Первый аргумент должен быть int

    def test_missing_arguments(self):
        """Тест на отсутствие аргументов"""
        with self.assertRaises(TypeError):
            sum_two()  # Не передан ни один аргумент

        with self.assertRaises(TypeError):
            sum_two(1)  # Второй аргумент отсутствует

    def test_extra_arguments(self):
        """Тест на наличие лишних аргументов"""
        with self.assertRaises(TypeError):
            sum_two(1, 2, 3)  # Третий аргумент лишний

if __name__ == '__main__':
    unittest.main()
