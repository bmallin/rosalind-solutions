from collections import Counter

DNA_BASE_PAIR_COMPLEMENTS = {
    'A': 'T',
    'C': 'G',
    'T': 'A',
    'G': 'C'
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
    dna_strings = []
    for line in fasta_file:
        line = line.strip()

        if line.startswith('>'):
            if current_id:
                dna_strings.append((current_id, current_dna_string))
                current_dna_string = ''

            current_id = line[1:]
        else:
            current_dna_string += line

    dna_strings.append((current_id, current_dna_string))

    return dna_strings


if __name__ == '__main__':
    pass
