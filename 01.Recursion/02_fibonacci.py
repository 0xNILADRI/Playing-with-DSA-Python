def fibonacci(nTerms):
    assert nTerms>=0 and int(nTerms)==nTerms, "The number should be integer and greater than 0"

    if nTerms in [0,1]:
        return nTerms
    else:
        return fibonacci(nTerms-1) + fibonacci(nTerms-2)

nTerm = 10

for i in range(nTerm):
    print(fibonacci(i))