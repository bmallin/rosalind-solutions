from bioinformatics.genetics import gc_content
from bioinformatics.genetics import parse_fasta


with open('data/computing_gc_content.txt') as file_handle:
    dna_strings = parse_fasta(file_handle)

gc_contents = [(id_, gc_content(dna_string))
               for id_, dna_string in dna_strings]

print(*sorted(gc_contents, key=lambda x: x[1])[-1], sep='\n')
