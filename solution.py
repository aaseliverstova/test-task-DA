# Задание 1
def is_isomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    map_st = {}
    map_ts = {}
    for cs, ct in zip(s, t):
        if cs in map_st and map_st[cs] != ct:
            return False
        if ct in map_ts and map_ts[ct] != cs:
            return False
        map_st[cs] = ct
        map_ts[ct] = cs
    return True

# Задание 2
def missing_number(nums):
    n = len(nums) + 1  
    expected = n * (n + 1) // 2
    actual = sum(nums)
    return expected - actual

# Задание 3
def prime_factors(n: int):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors
