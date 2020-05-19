def isoddeven(n):
    for i in range(1, n+1):
        if i % 2 == 0:
            print(i, 'is an even number')
        else:
            print(i, 'is an odd number')
    return('')


n = int(input())
print(isoddeven(n))
