from collections import Counter

with open('data/counting_dna_nucleotides.txt') as file_handle:
    dna_string = file_handle.read()

base_counts = Counter(dna_string)

print(
    base_counts.get('A'),
    base_counts.get('C'),
    base_counts.get('G'),
    base_counts.get('T'),
)
