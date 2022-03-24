import unittest
from randomFunktions import my_sum


class TestMyTry(unittest.TestCase):

    def testSumEasy(self):
        self.assertEqual(my_sum.sum([2, 5]), 7)

    def test_bad_type(self):
        data = "bananana"
        with self.assertRaises(TypeError):
            result = my_sum.sum(data)
            print(result)


if __name__ == '__main__':

    unittest.main()
