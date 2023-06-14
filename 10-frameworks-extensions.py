#test_framework is a fictitious library for didactic purposes
import test_framework

def assert_element_present(self, locator):
    if not self.is_element_present(locator):
        raise AssertionError(f"Element {locator} is not present on the page")

# Monkey patch the test case class
test_framework.TestCase.assert_element_present = assert_element_present