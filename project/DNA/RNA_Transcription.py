def to_rna(dna):
    '''
    >>> to_rna('AGT')
    'TCA'
    >>> to_rna('A   GT')
    'T   CA'
    '''
    DNA = {"A": "T", "C": "G", "G": "C", "T": "A", "a": "t", "c": "g", "g": "c", "t": "a", " ": " "}
    letters = str(dna)
    letters = [DNA[base] for base in letters]
    return ''.join(letters)


