## Lab02 TESTER ##

import sys
import os
import unittest

def main():
    # Check for the correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: python tester.py <function.py>")
        sys.exit(1)

    # Check if the file exists
    if not os.path.exists(sys.argv[1]):
        print(f"Error: File '{sys.argv[1]}' not found!")
        sys.exit(1)

    # Check if the file is a python file
    if not sys.argv[1].endswith(".py"):
        print(f"Error: File '{sys.argv[1]}' is not a python file!")
        sys.exit(1)

    # Run the tests
    run_tests(sys.argv[1])

def run_tests(file):
    # Dynamically import the module
    import importlib.util
    spec = importlib.util.spec_from_file_location("function", file)
    function = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(function)

    # Define the test cases
    class TestMakeBricks(unittest.TestCase):
        def test_case1(self):
            self.assertTrue(function.makeBricks(3, 1, 8))
        
        def test_case2(self):
            self.assertFalse(function.makeBricks(3, 1, 9))
        
        def test_case3(self):
            self.assertTrue(function.makeBricks(3, 2, 10))
        
        def test_case4(self):
            self.assertTrue(function.makeBricks(3, 2, 11))
        
        def test_case5(self):
            self.assertTrue(function.makeBricks(6, 1, 11))
        
        def test_case6(self):
            self.assertTrue(function.makeBricks(0, 3, 10))
        
        def test_case7(self):
            self.assertFalse(function.makeBricks(0, 3, 9))
        
        def test_case8(self):
            self.assertFalse(function.makeBricks(1, 4, 12))
        
        def test_case9(self):
            self.assertTrue(function.makeBricks(2, 2, 7))

    # Add the test case to the test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMakeBricks)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    main()