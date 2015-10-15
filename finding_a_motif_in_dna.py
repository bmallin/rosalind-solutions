def find_all(needle, haystack):
    rv = []
    window_size = len(needle)

    for window_start in range(len(haystack)):
        potential_match = haystack[window_start:window_start + window_size]
        if potential_match == needle:
            rv.append(window_start + 1)

    return rv

with open('data/finding_a_motif_in_dna.txt') as fp:
    dna_string, needle = map(str.strip, fp.readlines())

print(*find_all(needle, dna_string))
