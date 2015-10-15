def dominant_trait_probability(k, n, m):
    p = 1
    t = k + m + n

    p -= 0.25 * (m / t) * ((m - 1) / (t - 1))
    p -= 0.5 * (n / t) * (m / (t - 1))
    p -= 0.5 * (m / t) * (n / (t - 1))
    p -= (n / t) * ((n - 1) / (t - 1))

    return p


with open('data/mendels_first_law.txt') as file_handle:
    k, m, n = map(int, file_handle.read().strip().split())

print(dominant_trait_probability(k, m, n))
