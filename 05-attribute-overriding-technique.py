class BaseTestCase:
    timeout = 10  # Common timeout value for test cases

# Derived class: CustomTestCase
class CustomTestCase(BaseTestCase):
    pass

# Monkey patching: Attribute overriding
CustomTestCase.timeout = 20  # Override timeout for specific test cases