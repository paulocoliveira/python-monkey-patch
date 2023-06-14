class TestSuite:
    def __init__(self, name, test_cases, test_data, configuration):
        self.name = name
        self.test_cases = test_cases
        self.test_data = test_data
        self.configuration = configuration
    
    def run_tests(self):
        # Logic to execute the test cases in the test suite
        print("Running tests in", self.name)
        for test_case in self.test_cases:
            print("Running test case:", test_case)
            # Execute the test case using the test data and configuration
            # ...
            # ...


# Example of creating test suite objects
# Test Suite 1
test_cases_1 = ["Test Case 1", "Test Case 2", "Test Case 3"]
test_data_1 = {"input": "data1", "expected_output": "result1"}
configuration_1 = {"timeout": 10, "retries": 3}

suite_1 = TestSuite("Test Suite 1", test_cases_1, test_data_1, configuration_1)

# Test Suite 2
test_cases_2 = ["Test Case 4", "Test Case 5"]
test_data_2 = {"input": "data2", "expected_output": "result2"}
configuration_2 = {"timeout": 5, "retries": 2}

suite_2 = TestSuite("Test Suite 2", test_cases_2, test_data_2, configuration_2)

# Running the test suites
suite_1.run_tests()
suite_2.run_tests()
