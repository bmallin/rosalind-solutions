from bioinformatics.genetics import DNA_BASE_PAIR_COMPLEMENTS

with open('data/complementing_a_strand_of_dna.txt') as file_handle:
    dna_string = file_handle.read().strip()

print(''.join(
    map(
        lambda x: DNA_BASE_PAIR_COMPLEMENTS[x],
        reversed(dna_string)
    )
))
