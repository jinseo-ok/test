import unittest

import main

class MaiTest(unittest.TestCase):

    def test_helloworld(self):
        ret = main.helloworld("TEST")
        self.assertEqual(ret, "Hello World! Chris")


if __name__ ==  "__main__":
    unittest.main()