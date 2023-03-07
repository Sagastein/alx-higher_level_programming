#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE Sagacode

lastdigit = int(str(number)[-1])

if lastdigit > 5:
    print("Last digit of "+ str(number) +" is "+ str(lastdigit) +" and is greater than 5")
elif lastdigit == 0:
    print("Last digit of "+ str(number) +" is "+ str(lastdigit) +" and is 0")
else:
    print("Last digit of "+ str(number) +" is "+ str(lastdigit) +" and is less than 6 and not 0")
