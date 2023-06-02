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
    
    def test_degrees_Test(self):
        self.assertEqual(degrees_easy.pi(50), 2864)
        