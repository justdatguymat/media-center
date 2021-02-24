import unittest
from io import StringIO
from media_center.main import main

class TestMain(unittest.TestCase):
    def test_main(self):
        main()
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
