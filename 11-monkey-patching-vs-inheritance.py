# Base test class
class BaseTest:
    def run_test(self):
        print("Running base test...")

# Derived test class inheriting from BaseTest
class SmokeTest(BaseTest):
    def run_test(self):
        print("Running smoke test...")

# Monkey patching the BaseTest class
def monkey_patch_run_test(self):
    print("Monkey patch run test")

BaseTest.run_test = monkey_patch_run_test

# Creating instances and running tests
base_test = BaseTest()
smoke_test = SmokeTest()

base_test.run_test()   # Output: Monkey patch run test
smoke_test.run_test()  # Output: Running smoke test...
