import pprint
from collections import Counter
from bioinformatics.genetics import parse_fasta


class ProfileMatrix:
    def __init__(self, dna_strings: list):
        self._matrix = []
        for row in zip(*dna_strings):
            count = Counter(row)
            self._matrix.append([
                count['A'],
                count['C'],
                count['G'],
                count['T']])

        self._consensus = ''

    def __str__(self):
        return pprint.pformat(list(zip(*self._matrix)))

    @property
    def consensus(self):
        possibles = list('ACGT')
        parts = []
        for row in self._matrix:
            most_common = max(range(len(row)), key=row.__getitem__)
            parts.append(possibles[most_common])

        return ''.join(parts)

    @consensus.setter
    def consensus(self, value):
        raise TypeError('Profile matrix object does not support assignment.')

with open('data/consensus_and_profile.txt') as fp:
    p = ProfileMatrix(parse_fasta(fp).values())
    print(p.consensus)
