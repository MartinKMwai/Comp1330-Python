a=int(input())
b=int(input())
c=int(input())
if a==b==c:
    print("equilateral")
elif a+b<=c or a+c<=b or b+c<=a:
    print("impossible")
elif a==b or a==c or b==c:
    print("isosceles")
elif a+b<=c or a+c<=b or b+c<=a:
    print("impossible")
else:
    print("scalene")
