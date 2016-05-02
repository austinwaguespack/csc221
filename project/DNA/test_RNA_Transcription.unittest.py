import unittest
from RNA_Transcription import to_rna

class Test_to_rna(unittest.TestCase):
    def setUp(self):
        pass
    def test_rna_transcription(self):
        self.assertEqual( to_rna('AGT'), 'TCA')
    def test_rna_transcription_with_space(self):
        self.assertEqual( to_rna('A  GT'), 'T  CA')

if __name__ == '__main__':
    unittest.main()
