   
# from mockito import mock, verify
# import unittest

# from helloworld import helloworld

# class HelloWorldTest(unittest.TestCase):
#        def test_should_issue_hello_world_message(self):
#            out = mock()

#            helloworld(out)

#            verify(out).write("Hello world of Python\n")


import unittest
import io
import sys
# from helloworld import helloworld  # Adjust the import based on the actual module name
from helloworld import helloworld
class TestHelloWorld(unittest.TestCase):

    def test_helloworld(self):
        # Create a StringIO object to capture the output
        output = io.StringIO()

        # Call the function with the StringIO object
        helloworld(output)

        # Get the value written to the StringIO object
        result = output.getvalue()

        # Expected output
        expected = "Hello world of Python\n"

        # Assert that the expected output matches the result
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()



