x=[1, 3, 5, 9, 7, 8, 2, 6, 3, 11]
y=int(input())
if y<=len(x) and y>0:
    print(x[y-1])

else:
    print("Error: Invalid Input")
