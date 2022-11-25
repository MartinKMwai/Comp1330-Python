x=[1,3,5,9,7,8,2,6,3,11]
y=int(input())
z=-1
for w in range(len(x)):
    #w=0,1,2,3,4,5,6,7,8,9 len-x
    if y==x[w]:
        z=w
        break;
    #else:
    #    print(-x)
print(z)
