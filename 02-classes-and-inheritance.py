class TestSuite:
    def __init__(self, name):
        self.name = name

    def run_tests(self):
        print("Running tests in", self.name)


class RegressionTestSuite(TestSuite):
    def run_tests(self):
        print("Running regression tests in", self.name)
        # Additional regression test logic


class SmokeTestSuite(TestSuite):
    def run_tests(self):
        print("Running smoke tests in", self.name)
        # Additional smoke test logic


class PerformanceTestSuite(TestSuite):
    def run_tests(self):
        print("Running performance tests in", self.name)
        # Additional performance test logic


# Example of creating objects and using functions
regression_suite = RegressionTestSuite("Regression Test Suite")
smoke_suite = SmokeTestSuite("Smoke Test Suite")
performance_suite = PerformanceTestSuite("Performance Test Suite")

regression_suite.run_tests()
smoke_suite.run_tests()
performance_suite.run_tests()
