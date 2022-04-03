def factorial(n):
    assert n>=0 and int(n)==n, "The number should be greater than 0 and integer"

    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(4))