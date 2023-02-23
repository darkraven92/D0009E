#Iteration
def bounce2(n):
    for i in range(n, -1, -1):
        print(i, end=" ")
    for i in range(1, n + 1):
        print(i, end=" ")

bounce2(7)
