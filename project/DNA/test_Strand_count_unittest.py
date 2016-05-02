import unittest
from collections import Counter
from Strand_count import rna_count
class TestSC(unittest.TestCase):
     def setUp(self):
        pass
     def test_strand_return(self):
        self.assertEqual( rna_count('AGTC'), Counter({'A': 1, 'C': 1, 'T': 1, 'G': 1}))
     def test_strand_return_with_white(self):
        self.assertEqual( rna_count('AG TC'), Counter({'A': 1, 'C': 1, 'T': 1, 'G': 1}))

if __name__ == '__main__':
    unittest.main()    
