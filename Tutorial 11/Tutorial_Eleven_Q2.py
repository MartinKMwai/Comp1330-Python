def bubsort(array):
    lenofarray = len(array)-1
    for i in range (lenofarray):
        for j in range (lenofarray-i):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
    return array
arr=[]
n=int(input())
for i in range(n):
    integers=input()
    inn=integers.split(' ')
    tup=tuple(inn)
    arr.append(tup)

arr = bubsort(arr)
for i in range (len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end=' ')
    print()

