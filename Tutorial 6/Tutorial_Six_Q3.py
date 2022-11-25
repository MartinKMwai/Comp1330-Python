a=[]
average=0.0
x=int(input("Number of students? "))
for y in range(x):
    print(f"Student {y+1}: ",end="")
    b=int(input())
    a.append(b)
    average+=b
average=average/x
print(f"Average={average:0.2f}")
for c in range(x):
    for b in range(a[c]):
        print('*',end="")
    print()
    

    
    
           
           
