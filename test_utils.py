# test_utils.py
# Author: Sébastien Combéfis
# Version: February 2, 2016

import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_fact(self):
        with self.assertRaises(ValueError):
           utils.fact(-1)
        pass
    
    def test_roots(self):
        # À compléter...
        pass
    
    def test_integrate(self):
        assert lower > upper, "Problèmes aux bornes!"
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
