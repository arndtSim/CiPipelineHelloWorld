import unittest
from randomFunktions import my_sum


## @class TestMyTry
# @brief Class for all unittests.
#
# This class provides several unittests for testing
# each unit of the created code.
class TestMyTry(unittest.TestCase):

    ## @brief tests easy summation
    def testSumEasy(self):
        self.assertEqual(my_sum.sum([2, 5]), 7)

    ## @brief tests bad input types
    def test_bad_type(self):
        data = "bananana"
        with self.assertRaises(TypeError):
            result = my_sum.sum(data)
            print(result)


if __name__ == '__main__':

    unittest.main()
