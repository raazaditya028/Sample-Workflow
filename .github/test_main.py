import unittest
from main import add

class TestMain(unittest.TestCase):
    def test_add(self):
        assert add(2,3) == 5
        assert add(-2,2) == 0


# If the expected output and actual output is same then we will get the result as pass.
# Assert is assertion function with checking actual == expected
# If it matches test cases passed.
# To run this we wil use a command  i.e. pytest.