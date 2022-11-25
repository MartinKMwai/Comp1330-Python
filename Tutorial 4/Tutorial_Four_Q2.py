number = int(input())
counter = 0
if(number>0):
    for value in range(2, number-1):
        if(number%value == 0):
            counter += 1
    print (counter)
else:
    for value in range(number < 0):
        print("Error: Negative number")
     

