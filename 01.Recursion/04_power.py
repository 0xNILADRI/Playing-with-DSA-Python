def power(num, exp):
    assert num>=1 and int(exp)==exp , "The base should be greeater than 0 and exponent should be integer"
    if exp == 0:
        return 1
    if exp == 1:
        return num
    return num * power(num,exp-1)

print(power(2,3))