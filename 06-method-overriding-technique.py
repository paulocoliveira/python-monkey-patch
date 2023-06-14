class BaseTestCase:
    def run_test(self):
        print("Common test execution logic")

# Derived class: CustomTestCase
class CustomTestCase(BaseTestCase):
    def run_test(self):
        print("Additional setup steps")
        # Call base class method
        super().run_test()
        print("Additional teardown steps")