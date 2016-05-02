from collections import Counter
def rna_count(dna):
    '''
    >>> rna_count('AGTC')
    Counter({'A': 1, 'C': 1, 'T': 1, 'G': 1})
    >>> rna_count('AG TC')
    Counter({'A': 1, 'C': 1, 'T': 1, 'G': 1})
    '''
    S = list(dna.strip())
    S = dna.replace(" ","")
    DNA = {"A": "T", "C": "G", "G": "C", "T": "A", "a": "t", "c": "g", "g": "c", "t": "a"}
    letters = str(S)
    letters = [DNA[base] for base in letters]
    d = Counter(S)
    return d

