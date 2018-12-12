import unittest

class MyFirstUnit(unittest.TestCase):

   def testcase1(self):
        self.assertEqual("20","20")   #assert断言
if __name__ == "__main__":
    unittest.main()


