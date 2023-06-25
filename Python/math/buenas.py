import unittest

class MathDojo:
    def __init__(self):
        self.resultado = 0

    def suma(self, *args):
        for num in args:
            self.resultado += num
        return self

    def resta(self, *args):
        for num in args:
            self.resultado -= num
        return self

class MathDojoTests(unittest.TestCase):
    def setUp(self):
        self.md = MathDojo()

    def test_suma(self):
        self.assertEqual(self.md.suma(2, 4, 6).resultado, 12)
        self.assertEqual(self.md.suma(1, 2).resultado, 15)

    def test_resta(self):
        self.assertEqual(self.md.resta(5, 3).resultado, -8)
        self.assertEqual(self.md.resta(10).resultado, -18)

    def test_suma_y_resta(self):
        self.assertEqual(self.md.suma(5, 10).resta(3, 2).resultado, 10)
        self.assertEqual(self.md.suma(1, 2, 3).resta(6, 1).resultado, -1)

if __name__ == "__main__":
    unittest.main()
