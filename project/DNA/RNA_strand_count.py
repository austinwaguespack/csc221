import re

def rna_strand_count(dna,strands):
    '''
    >>> rna_strand_count('AAAA', 'AA')
    {'AA': 3}
    >>> rna_strand_count('ATCG', 'AA')
    {'AA': 0}
    >>> rna_strand_count('A AA A', 'AA')
    {'AA': 3}
    '''
    dna = dna.replace(' ','').upper()
    strands = strands.replace(' ','').upper()
    first = strands[0]
    second = strands[1:]
    return {strands:len(re.findall(r'{0}(?={1})'.format(first,second),dna))}


