import unittest
from RNA_strand_count import rna_strand_count

class Test_RNA_strand(unittest.TestCase):
    def setUp(self):
        pass
    def test_rna_strand_count(self):
        self.assertEqual( rna_strand_count('AAAA', 'AA'), {'AA': 3})
    def test_rna_no_match(self):
        self.assertEqual( rna_strand_count('ACGT', 'AA'), {'AA': 0})
    def test_rna_strand_count_with_white(self):
        self.assertEqual( rna_strand_count('A A A A', 'AA'), {'AA': 3})

if __name__ == '__main__':
    unittest.main()
