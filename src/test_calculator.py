import unittest
from calculator import add

class TestCalculator(unittest.TestCase):
    def test_add(self):
        # Ми кажемо: "Перевір, чи дорівнює результат додавання 2 і 3 числу 5"
        # Якщо так - тест пройдено. Якщо ні - Jenkins видасть помилку!
        self.assertEqual(add(2, 3), 9)

if __name__ == '__main__':
    unittest.main()