import collections


def mortal_fib(n, m):
    a, b = 0, 1
    losses = collections.deque()
    for i in range(n):
        b, a = a + b, b
        losses.append(b)

        if i >= m:
            loss = losses.popleft()
            a -= loss

    return a


with open('data/mortal_fibonacci_rabbits.txt') as fp:
    n, m = map(int, fp.read().strip().split())

print(mortal_fib(n, m))
