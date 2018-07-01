def bounce(n):
    if not n:
        print(n, end = " ")
        return
    print(n, end = " ")
    bounce(n-1)
    print(n, end = " ")

#bounce(0)

def bounce2(n):
    k = n
    while n > 0:
        print(n, end = " ")
        n = n - 1
    while n <= k:
        print(n, end = " ")
        n = n + 1
#bounce2(3)

def tvarsumma(n):
    if n == 0:
        return 0
    else:
        return (n%10)+tvarsumma(n//10)

#print(tvarsumma(99))

def tvarsumma2(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

#print(tvarsumma2(12))

def derivative(f,x,h):
    return 1.0 / (2 * h) * (f(x + h) - f(x - h))

#print(derivative(math.sin,math.pi,0.0001))

def solve(f,x0,h):
    x = 0
    while True:
        x = x0 - (f(x0) / derivative(f, x0, h))
        if abs(x - x0) < h:
            return x
        x0 = x
