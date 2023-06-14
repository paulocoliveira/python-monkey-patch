# Decorator function for test logging
def log_test(func):
    def wrapper():
        print("Logging test...")
        return func()
    return wrapper

# Test function with decorator
@log_test
def perform_test():
    print("Performing test...")

# Running the original test
perform_test()  # Output: Logging test... Performing test...

# Monkey patching a test function
def monkey_patch_test():
    print("Monkey patch test")

perform_test = monkey_patch_test

# Running the modified test
perform_test()  # Output: Monkey patch test