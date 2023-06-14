from selenium.webdriver.remote.webelement import WebElement

# Monkey patching: Adding a custom method to the WebElement class
def highlight_element(self):
    self._execute_script("arguments[0].style.border='2px solid red';", self)

WebElement.highlight_element = highlight_element