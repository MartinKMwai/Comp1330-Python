Sec= int ( input("Please enter the number of seconds: "))
Hours = int (Sec / 3600)
MinA = int (Sec % 3600)
MinB = int (MinA / 60)
Seconds= int(MinA % 60)
print(str(Sec)  + " second(s) = " + str(Hours)+ " hour(s) " + str(MinB) + " minute(s) "+ str(Seconds) + " second(s)" )





