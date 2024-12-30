from __future__ import annotations
def diophantine(a: int, b: int, c: int) -> tuple[float, float]:
    assert (c % greatest_common_divisor(a, b) == 0)
    (d, x, y) = extended_gcd(a, b) 
    r = c / d
    return (r * x, r * y)
def diophantine_all_soln(a: int, b: int, c: int, n: int = 2) -> None:
    (x0, y0) = diophantine(a, b, c)  # Initial value
    d = greatest_common_divisor(a, b)
    p = a // d
    q = b // d
    for i in range(n):
        x = x0 + i * q
        y = y0 - i * p
        print(x, y)
def greatest_common_divisor(a: int, b: int) -> int: # nuance
    if a < b:
        a, b = b, a
    while a % b != 0:
        a, b = b, a % b
    return b
def extended_gcd(a: int, b: int) -> tuple[int, int, int]: # test
    assert a >= 0 and b >= 0
    if b == 0:
        d, x, y = a, 1, 0
    else:
        (d, p, q) = extended_gcd(b, a % b)
        x = q
        y = p - q * (a // b)
    assert a % d == 0 and b % d == 0
    assert d == a * x + b * y
    return (d, x, y)
if __name__ == "__main__":
    from doctest import testmod
    testmod(name="diophantine", verbose=True)
    testmod(name="diophantine_all_soln", verbose=True)
    testmod(name="extended_gcd", verbose=True)
    testmod(name="greatest_common_divisor", verbose=True)
# eof
