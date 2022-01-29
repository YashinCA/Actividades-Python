import unittest
from TDDMathdojo import MathDojo

# 1. El resultado al crear la instancia, es cero


class TestsMathdojo(unittest.TestCase):

    def testTwo(self):
        md = MathDojo()
        self.assertEqual(md.result, 0)

    def testThree(self):
        md = MathDojo()
        self.assertNotEqual(md.result, 20)

    def setUp(self):
        print("running setUp")

    def tearDown(self):
        print("running tearDown tasks")


if __name__ == '__main__':
    unittest.main()


# 2. El resultado de add para 2 es 2 y para (2,5,1) es 8
class TestsMathdojo(unittest.TestCase):

    def testTwo(self):
        md = MathDojo()
        self.assertEqual(md.add(2).result, 2)

    def testThree(self):
        md = MathDojo()
        self.assertNotEqual(md.add(8, 6, 1).result, 25)

    def testFour(self):
        md = MathDojo()
        self.assertEqual(md.add(2, 5, 1).result, 8)

    def setUp(self):
        print("running setUp")

    def tearDown(self):
        print("running tearDown tasks")


if __name__ == '__main__':
    unittest.main()

# 3. El resultado de subtract(3, 2) es -5


class TestsMathdojo(unittest.TestCase):

    def testTwo(self):
        md = MathDojo()
        self.assertEqual(md.subtract(3, 2).result, -5)

    def testThree(self):
        md = MathDojo()
        self.assertNotEqual(md.subtract(3, 2).result, 25)

    def testFour(self):
        md = MathDojo()
        self.assertEqual(md.subtract(6, 9).result, -15)

    def setUp(self):
        print("running setUp")

    def tearDown(self):
        print("running tearDown tasks")


if __name__ == '__main__':
    unittest.main()

# 3. El resultado de subtract(3, 2) es -5


class TestsMathdojo(unittest.TestCase):

    def testTwo(self):
        md = MathDojo()
        self.assertEqual(md.add(2).add(2, 5, 1).subtract(3, 2).result, 5)

    def testThree(self):
        md = MathDojo()
        self.assertNotEqual(md.add(2).add(2, 5, 1).subtract(3, 2).result, 25)

    def testFour(self):
        md = MathDojo()
        self.assertEqual(md.add(8).add(5, 4, 9).subtract(10, 9).result, 7)

    def setUp(self):
        print("running setUp")

    def tearDown(self):
        print("running tearDown tasks")


if __name__ == '__main__':
    unittest.main()
