import unittest
import CodingInterview_hard
import degrees_easy
import discount_easy
import lengthofNumber_medium
import sum_very_easy
import triangle_very_easy
import UpDpwnHill_hard
import ViryualDAC_medium

class Challanges_Unit_Tests(unittest.TestCase):
    def test_Discount(self):
        self.assertEquals(discount_easy.dis(100, 50), 50)
        
    def test_CodingInterview(self):
        self.assertEqual(CodingInterview_hard.interview([5, 5, 10, 10, 15, 15, 20, 20], 120), "qualified")
    
    def test_sum(self):
       self.assertEqual(sum_very_easy.addition(3, 4), 7)

    def test_triangle(self):
        self.assertEqual(triangle_very_easy.tri_area(4,4), 8)

    def test_degrees(self):
        self.assertEqual(degrees_easy.radians_to_degrees(20), 1146)

    def test_length(self):
        self.assertEqual(lengthofNumber_medium.number_length(123), 3)

    def test_hill(self):
        self.assertEqual(UpDpwnHill_hard.ave_spd(18, 20, 60), 30)

    def test_Dac(self):
        self.assertEqual(ViryualDAC_medium.V_DAC(1023), 5)
