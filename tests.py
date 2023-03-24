import unittest
from random import randint
from main import destructure


def generate_nested_list(stack=[], level=10):
    stack.append(randint(1, 5))
    if level > 0:
        stack.append(generate_nested_list([], level=level - 1))
    return stack


class TestDestructure(unittest.TestCase):
    def test_basic(self):
        result = destructure([1, [2, [3, [4, 5]]]])
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_random(self):
        result = destructure(generate_nested_list(level=randint(1, 50)))
        self.assertEqual(all(isinstance(el, int) for el in result), True)
        self.assertEqual(any(isinstance(el, list) for el in result), False)

    def test_random_stress(self):
        result = destructure(generate_nested_list(level=950))
        self.assertEqual(all(isinstance(el, int) for el in result), True)
        self.assertEqual(any(isinstance(el, list) for el in result), False)

    def test_empty_lists(self):
        result = destructure([[[], [[[]], []], [[[[]]], [1]]]])
        self.assertEqual(result, [1])

    @unittest.expectedFailure
    def test_iterable_error(self):
        destructure(100)


if __name__ == "__main__":
    unittest.main()
