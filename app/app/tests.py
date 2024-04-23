from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    
    def test_add_nos(self):
        res =   calc.add(5, 6)
        self.assertEqual(res, 11)
        
    def test_mul_nos(self):
        res = calc.multiply(9, 8)  
        self.assertEqual(res, 72)
        
    def test_subtract_nos(self):
        res  = calc.subtract(10, 4)
        self.assertEqual(res, 6)