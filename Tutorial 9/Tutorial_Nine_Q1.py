n=int(input())
totalarea=0
def rectarea(r):
    return r[2]*r[3]
for i in range (n):
    s=input().split()
    numbers=[int(item) for item in s]
    t= tuple(numbers)
    totalarea+=rectarea(t)

print (totalarea)
