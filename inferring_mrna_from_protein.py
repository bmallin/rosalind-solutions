from bioinformatics.genetics import AMINO_ACID_TO_RNA_CODON


def count_possible_rna_strings(protein, modulus):
    n = len(AMINO_ACID_TO_RNA_CODON['Stop'])
    for amino_acid in protein:
        n *= len(AMINO_ACID_TO_RNA_CODON[amino_acid])

    return n % modulus


with open('data/inferring_mrna_from_protein.txt') as fp:
    protein = fp.read().strip()

    print(count_possible_rna_strings(protein, 10**6))
