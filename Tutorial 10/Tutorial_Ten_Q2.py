def prime(n,i):
    # exit case
    if i==1:
        return True
    #n-1/n+1 case
    if n%i==0:
        return False
    return (n,i-1)
        
    #current case
    

n=int(input())
if prime(n,n//2):
    print('true')
else:
    print('false')
