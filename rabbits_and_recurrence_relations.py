def calc_rabbit_pairs(n: int, k: int) -> int:
    a, b = 0, 1
    for i in range(n):
        b, a = k * a + b, b

    return a


with open('data/rabbits_and_recurrence_relations.txt') as file_handle:
    n, k = map(int, file_handle.read().split())

print(calc_rabbit_pairs(n, k))
