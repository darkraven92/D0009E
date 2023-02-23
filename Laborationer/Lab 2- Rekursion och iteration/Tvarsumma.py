def tvarsumman(n):
    if n < 10:
        return n
    else:
        return n % 10 + tvarsumman(n // 10)
    
tvarsumman(123)

#Iterativ
def tvarsumman2(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

