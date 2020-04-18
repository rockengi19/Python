#This program calculates the average of twenty integer numbers in a random list

import random

def Mean(stp):
    average = 0
    summing = 0
    for i in range(len(stp)):
        summing += stp[i]
        average = summing/len(stp)
    return "The average is",average

stp = []
for j in range(20):
    stp.append(random.randint(0,120))

print("The random list is",stp)
print(Mean(stp))
