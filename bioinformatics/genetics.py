from collections import Counter
from collections import OrderedDict


DNA_BASE_PAIR_COMPLEMENTS = {
    'A': 'T',
    'C': 'G',
    'T': 'A',
    'G': 'C'
}


RNA_CODON_TABLE = {
    'UUU': 'F',
    'UUC': 'F',
    'UUA': 'L',
    'UUG': 'L',
    'UCU': 'S',
    'UCC': 'S',
    'UCA': 'S',
    'UCG': 'S',
    'UAU': 'Y',
    'UAC': 'Y',
    'UAA': 'Stop',
    'UAG': 'Stop',
    'UGU': 'C',
    'UGC': 'C',
    'UGA': 'Stop',
    'UGG': 'W',
    'CUU': 'L',
    'CUC': 'L',
    'CUA': 'L',
    'CUG': 'L',
    'CCU': 'P',
    'CCC': 'P',
    'CCA': 'P',
    'CCG': 'P',
    'CAU': 'H',
    'CAC': 'H',
    'CAA': 'Q',
    'CAG': 'Q',
    'CGU': 'R',
    'CGC': 'R',
    'CGA': 'R',
    'CGG': 'R',
    'AUU': 'I',
    'AUC': 'I',
    'AUA': 'I',
    'AUG': 'M',
    'ACU': 'T',
    'ACC': 'T',
    'ACA': 'T',
    'ACG': 'T',
    'AAU': 'N',
    'AAC': 'N',
    'AAA': 'K',
    'AAG': 'K',
    'AGU': 'S',
    'AGC': 'S',
    'AGA': 'R',
    'AGG': 'R',
    'GUU': 'V',
    'GUC': 'V',
    'GUA': 'V',
    'GUG': 'V',
    'GCU': 'A',
    'GCC': 'A',
    'GCA': 'A',
    'GCG': 'A',
    'GAU': 'D',
    'GAC': 'D',
    'GAA': 'E',
    'GAG': 'E',
    'GGU': 'G',
    'GGC': 'G',
    'GGA': 'G',
    'GGG': 'G'
}


def hamming_distance(a, b):
    return sum((x != y for x, y in zip(a, b)))


def gc_content(dna_string):
    base_counter = Counter(dna_string)
    gc_count = base_counter.get('G') + base_counter.get('C')

    return (gc_count / len(dna_string)) * 100


def parse_fasta(fasta_file):
    current_id = ''
    current_dna_string = ''
    dna_strings = OrderedDict()
    for line in fasta_file:
        line = line.strip()

        if line.startswith('>'):
            if current_id:
                dna_strings[current_id] = current_dna_string
                # dna_strings.append((current_id, current_dna_string))
                current_dna_string = ''

            current_id = line[1:]
        else:
            current_dna_string += line

    # dna_strings.append((current_id, current_dna_string))
    dna_strings[current_id] = current_dna_string

    return dna_strings


if __name__ == '__main__':
    pass
