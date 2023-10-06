

def binary_num(n):
    assert int(n) == n, "parameter only takes integer"
    if n == 0:
        return n
    else:
        return n % 2 + 10 * binary_num(int(n/2))


print(binary_num(14))