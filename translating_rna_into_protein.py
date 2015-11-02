from bioinformatics.genetics import RNA_CODON_TABLE


def rna_to_protein(rna_string):
    amino_acids = []
    for i in range(0, len(rna_string), 3):
        codon = rna_string[i:i + 3]
        protein = RNA_CODON_TABLE[codon]

        if not protein == 'Stop':
            amino_acids.append(RNA_CODON_TABLE[codon])

    return ''.join(amino_acids)


with open('data/translating_rna_into_protein.txt') as fp:
    data = fp.read().strip()

print(rna_to_protein(data))
