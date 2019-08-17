import unittest
import letia.sample.calculation

class TestSample(unittest.TestCase):

    def test_calculate(self):
        self.assertEqual(letia.sample.calculation.calculate(7), 42)

if __name__ == "__main__":
    unittest.main()
