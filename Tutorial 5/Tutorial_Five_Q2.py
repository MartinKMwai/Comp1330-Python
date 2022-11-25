limit = int(input())

n = 1

while n <= limit:

    sum = 0
    divisor = 1
    while divisor < n:
        if not n % divisor:
            sum += divisor
        divisor = divisor + 1
    if sum == n:
        print(n, end=" ")
    n = n + 1
