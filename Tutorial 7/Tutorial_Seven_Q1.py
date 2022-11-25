x=int(input())
z=[]
y=[]

for v in range (x):
    u=int(input())
    if (u>=0 and u<=49):
        y.append(u)
    else:
        continue

for a in y:
    if a not in z:
        z.append(a)
y.sort()
z.sort()

for w in z:
    c=0
    for dp in y:
        if w==dp:
            c+=1
    if c!=2:
        print(w)
