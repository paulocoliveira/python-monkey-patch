class TestSuite:
    def run_tests(self):
        print("Running tests in the base TestSuite")

# Derived class: RegressionTestSuite
class RegressionTestSuite(TestSuite):
    def run_tests(self):
        print("Running regression tests")

def new_regression_test_method(self):
    print("Executing new regression test method")

RegressionTestSuite.new_method = new_regression_test_method

regression_suite = RegressionTestSuite()
regression_suite.run_tests()  # Existing overridden method
regression_suite.new_method()  # Newly added method
