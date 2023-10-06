def power_of(base, exp):
    assert exp>=0 and int(exp)==exp, 'choose the correct numbmer'
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        return base * power_of(base, exp-1)


print(power_of(2, 4))
