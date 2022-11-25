def bubsort(array):
    lenofarray=len(array)-1
    for i in range (lenofarray):
        for j in range (lenofarray-i):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
    return array

inp=input()
arr=[]
inn=inp.split(' ')
numb=[int(item) for item in inn]



bubsort(numb)
for i in range (len(numb)):
    print(numb[i], end=' ')
