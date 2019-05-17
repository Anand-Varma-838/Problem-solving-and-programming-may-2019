def fact(n):
    if n==1:
        return 1
    else :
        return fact(n-1)*n


def sumN(n):
    if n==1:
        return 1
    else:
        return n+sumN(n-1)