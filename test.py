import unittest
from cl_calculator import verify_input


class Test_input(unittest.TestCase):
    def test_input(self):
        self.assertTrue(verify_input("7+8+1979767564463232098097986764453"))
        self.assertTrue(verify_input("99**8+1979767564463232098097986764453"))
        self.assertFalse(verify_input("(h+165),(),//@3%7"))
        self.assertFalse(verify_input(".,()"))
        self.assertFalse(verify_input("77/"))

    def test_string(self):
        self.assertFalse(verify_input("mesopotamian tribe"))



if __name__ == "__main__":
    unittest.main()
