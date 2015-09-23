with open('data/transcribing_dna_into_rna.txt') as file_handle:
    print(file_handle.read().strip().replace('T', 'U'))
