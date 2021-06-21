import unittest

class mytest(unittest.TestCase):

    #
    # def mytest_setup(cls):
    #     print("executes before all test cases")
    #
    # def mysuit_teardown(cls):
    #     print("executes after all test cases")
    @classmethod
    def setUpClass(cls) -> None:
        print("I run before all test")

    @classmethod
    def tearDownClass(cls) -> None:
        print("prints after all test cases executed")

    def setUp(self) -> None:
        print("runs before every test cases")

    def tearDown(self) -> None:
        print(" I run after every test")

    def test_mytest(self):
        print("test 1")


    def test_2(self):
        print("test 2")

    def hello(self):
        print("i am hello")

if __name__ == "__main__":
    unittest.main()