m=int(input())
n=int(input())

for a in range (1, m+1):
    print ("%5d"%a, end="")

    for b in range (2, n+1):
        print ("%5d"%(a*b), end="")

    print()
