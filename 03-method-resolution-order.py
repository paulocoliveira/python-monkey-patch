class BaseTest:
    def run_test(self):
        print("Running base test")


class WebTest(BaseTest):
    def run_test(self):
        print("Running web test")


class MobileTest(BaseTest):
    def run_test(self):
        print("Running mobile test")


class HybridTest(WebTest, MobileTest):
    pass


# Creating an object of HybridTest
test = HybridTest()

# Calling the run_test method
test.run_test()

# Accessing the MRO
print(HybridTest.__mro__)