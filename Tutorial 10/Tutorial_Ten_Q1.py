def even(num):
    if num==0:
        return
    if num%2==0:
        print(f"{num}", end=" ")
    even(num-1);
    
n=int(input())
even(n)
