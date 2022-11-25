a=input()
b=a.split(',')
for c in b: 
    if c.isnumeric():
        print(int(c), end=" ")
    else:
        print(int(c,16),end=" ")
