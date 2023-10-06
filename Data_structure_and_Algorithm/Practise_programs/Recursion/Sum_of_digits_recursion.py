def sum_digit(n):
    assert n>=0 and int(n) ==  n,  'enter positive number'
    if n == 0:
        return n
    else:
        return int(n % 10) + sum_digit(int(n/10))    # attached png


print(sum_digit(43))
print(int(177/10))
