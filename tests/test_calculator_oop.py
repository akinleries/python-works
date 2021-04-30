import unittest
from calculate_oop import Calculator


class calculator_oop_test(unittest.TestCase):

        def test_add_result(self):
            self.assertEqual(Calculator.add(2, 3), 5)
            self.assertEqual(Calculator.add(-2, -3), -5)
            self.assertEqual(Calculator.add(-2, 3), 1)
            self.assertEqual(Calculator.add(5345676540, 323456745), 5345676540 + 323456745)

        def test_add_result_type(self):
            self.assertIsInstance(Calculator.add(2, 3), int)
            self.assertIsInstance(Calculator.add(-2, -3), int)
            self.assertIsInstance(Calculator.add(2, -3), int)
            self.assertIsInstance(Calculator.add(5345676540, 323456745), int)

        def test_add_non_int_type(self):
            with self.assertRaises(TypeError):
                Calculator.add(2, "wer")

        def test_subtract_result(self):
            self.assertEqual(Calculator.subtract(5, 2), 3)
            self.assertEqual(Calculator.subtract(3, 2), 1)
            self.assertEqual(Calculator.subtract(34, 24), 10)
            self.assertEqual(Calculator.subtract(5345676540, 323456745), 5345676540 - 323456745)

        def test_subtract_result_type(self):
            self.assertIsInstance(Calculator.subtract(5, 2), int)
            self.assertIsInstance(Calculator.subtract(3, 2), int)
            self.assertIsInstance(Calculator.subtract(34, 24), int)
            self.assertIsInstance(Calculator.subtract(5345676540, 323456745), int)

        def test_add_none_int_type(self):
            with self.assertRaises(TypeError):
                Calculator.subtract(2, "wer")

        def test_multiply_result(self):
            self.assertEqual(Calculator.multiply(5, 2), 10)
            self.assertEqual(Calculator.multiply(3, 2), 6)
            self.assertEqual(Calculator.multiply(10, 10), 100)
            self.assertEqual(Calculator.multiply(5345676540, 323456745), 5345676540 * 323456745)

        def test_multiply_result_type(self):
            self.assertIsInstance(Calculator.multiply(5, 2), int)
            self.assertIsInstance(Calculator.multiply(-3, -2), int)
            self.assertIsInstance(Calculator.multiply(34, 24), int)
            self.assertIsInstance(Calculator.multiply(5345676540, 323456745), int)

        def test_multiply_non_int_type(self):
            with self.assertRaises(TypeError):
                Calculator.multiply(2, "wer")

        def test_divide_result(self):
            self.assertEqual(Calculator.divide(10, 2), 5)
            self.assertEqual(Calculator.divide(6, 3), 2)
            self.assertEqual(Calculator.divide(10, 5), 2)
            self.assertEqual(Calculator.divide(5345676540, 323456745), 5345676540 / 323456745)

        def test_divide_result_type(self):
            self.assertIsInstance(Calculator.divide(5, 2), float)
            self.assertIsInstance(Calculator.divide(6, 2), float)
            self.assertIsInstance(Calculator.divide(10, 2), float)
            self.assertIsInstance(Calculator.divide(5345676540, 323456745), float)

        def test_divide_non_int_type(self):
            with self.assertRaises(TypeError):
                Calculator.divide(2, "wer")


if __name__ == '__main__':
    unittest.main()
