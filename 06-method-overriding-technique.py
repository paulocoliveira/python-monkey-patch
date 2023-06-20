from selenium import webdriver

# Base test case class
class BaseTestCase:
    def run_test(self):
        # Instantiate WebDriver
        driver = webdriver.Chrome()

        # Common test execution logic
        driver.get("https://www.example.com")

        # Close the browser
        driver.quit()


# Derived class: CustomTestCase
class CustomTestCase(BaseTestCase):
    def run_test(self):
        # Additional setup steps
        driver = webdriver.Chrome()
        driver.maximize_window()

        # Call base class method
        super().run_test()

        # Additional teardown steps
        driver.close()