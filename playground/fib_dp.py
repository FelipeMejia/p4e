MAXN = 100
found = [False] * MAXN
memo = [0] * MAXN


def fibo(n):
    if found[n]:
        return memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    found[n] = True
    memo[n] = fibo(n - 1) + fibo(n - 2)
    return memo[n]


print(fibo(7))
