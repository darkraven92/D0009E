#Rekursion
def bounce(n):
    if n == 0:
        print(0)
    else:
        print(n, end=" ")
        bounce(n - 1)
        print(n, end=" ")
bounce(7)
