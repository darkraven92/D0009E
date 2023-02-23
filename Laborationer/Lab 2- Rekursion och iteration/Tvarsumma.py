def tvarsumman(n):
    if n < 10:
        return n
    else:
        return n % 10 + tvarsumman(n // 10)
    
tvarsumman(123)
