import unittest
from calculate_functions import add
from calculate_functions import subtract
from calculate_functions import multiply
from calculate_functions import divide

class calculator_function_test(unittest.TestCase):
    def test_add_result(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-2, -3), -5)
        self.assertEqual(add(-2, 3), 1)
        self.assertEqual(add(5345676540, 323456745), 5345676540 + 323456745)


    def test_add_result_type(self):
        self.assertIsInstance(add(2, 3), int)
        self.assertIsInstance(add(-2, -3), int)
        self.assertIsInstance(add(2, -3), int)
        self.assertIsInstance(add(5345676540, 323456745), int)

    def test_add_non_int_type(self):
        with self.assertRaises(TypeError):
            add(2, "wer")

    def test_subtract_result(self):
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(subtract(3, 2), 1)
        self.assertEqual(subtract(34, 24), 10)
        self.assertEqual(subtract(5345676540, 323456745), 5345676540 - 323456745)

    def test_subtract_result_type(self):
        self.assertIsInstance(subtract(5, 2), int)
        self.assertIsInstance(subtract(3, 2), int)
        self.assertIsInstance(subtract(34, 24), int)
        self.assertIsInstance(subtract(5345676540, 323456745), int)

    def test_add_none_int_type(self):
        with self.assertRaises(TypeError):
            subtract(2, "wer")

    def test_multiply_result(self):
        self.assertEqual(multiply(5, 2), 10)
        self.assertEqual(multiply(3, 2), 6)
        self.assertEqual(multiply(10, 10), 100)
        self.assertEqual(multiply(5345676540, 323456745), 5345676540 * 323456745)


    def test_multiply_result_type(self):
        self.assertIsInstance(multiply(5, 2), int)
        self.assertIsInstance(multiply(-3, -2), int)
        self.assertIsInstance(multiply(34, 24), int)
        self.assertIsInstance(multiply(5345676540, 323456745), int)



    def test_add_non_int_type(self):
        with self.assertRaises(TypeError):
            multiply(2, "wer")


    def test_divide_result(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(10, 5), 2)
        self.assertEqual(divide(5345676540, 323456745), 5345676540 // 323456745)


    def test_divide_result_type(self):
        self.assertIsInstance(divide(5, 2), float)
        self.assertIsInstance(divide(6, 2), float)
        self.assertIsInstance(divide(10, 2), float)
        self.assertIsInstance(divide(5345676540, 323456745), float)



    def test_add_non_int_type(self):
        with self.assertRaises(TypeError):
            divide(2, "wer")


if __name__ == '__main__':
    unittest.main()
