# In this Python program there are a random list and a function which orders the list's numbers using the comb sort

import random

stp = [] #empty list
for j in range(20):
    num = random.randint(0,120) #this instruction puts integer numbers
    if num not in stp:
       stp.append(num)
       j += 1

print("The random list is",stp)

def combsort(stp):
    gap = len(stp)
    swap = True
    while gap > 1 or swap:
          gap = max(1,int(gap/1.25)) #minimum gap is 1
          swap = False 
          for i in range(len(stp)-gap):
              j = i + gap
              if stp[i] > stp[j]:
                 stp[i], stp[j] = stp[j], stp[i]
                 swap = True
    return "This is the ordered list", stp

print(combsort(stp))
