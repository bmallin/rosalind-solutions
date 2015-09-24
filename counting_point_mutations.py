from bioinformatics.genetics import hamming_distance

with open('data/counting_point_mutations.txt') as file_handle:
    dna_strings = file_handle.readlines()

print(hamming_distance(*dna_strings))
