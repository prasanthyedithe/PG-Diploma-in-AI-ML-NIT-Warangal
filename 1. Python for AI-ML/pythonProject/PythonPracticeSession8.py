from PythonPracticeSession7 import goldbach
import unittest
from unittest.mock import patch


class TestSum(unittest.TestCase):

    def test_goldbach(self):
        data = 44
        result = goldbach(data)
        print(result)
        self.assertEqual(result, "44=3+41")

    def test_goldbach_error(self):
        data = "44"
        result = goldbach(data)
        print(result)
        self.assertRaises(TypeError)

    @patch('PythonPracticeSession7.goldbach', return_value="44=3+51")
    def test_goldbach_mock(self,goldbach):
        data = 44
        result = goldbach(data)
        self.assertEqual(result, "44=3+51")

    if __name__ == '__main__':
        unittest.main()
