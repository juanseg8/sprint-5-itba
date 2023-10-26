import unittest
from rectangulo import Rectangulo

class TestGetAreaReectangule(unittest.TestCase):

    def setUp(self):
        self.rectangle = Rectangulo(2,3)

    def test_get_area(self):
        self.assertEqual(self.rectangle.get_area(), 6, "La funcion no devuelve lo esperado")
    
    def test_negative_case(self):
        self.rectangle.set_width(-1)
        self.rectangle.set_height(2)
        self.assertEqual(self.rectangle.get_area(), -1, "La funcion no devuelve lo esperado")
    
    def test_geq(self):
        self.rectangle.set_width(2)
        self.rectangle.set_height(50)
        self.assertGreaterEqual(self.rectangle.get_area(),100,"No, no es mayor o igual a 100")

    def test_assert_raises(self):
        with self.assertRaises(ZeroDivisionError):
            a = 1/0
    
    def tearDown(self):
        self.rectangle.cleanup()


if __name__ == "__main__":
    unittest.main()


