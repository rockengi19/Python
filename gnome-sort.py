# In this Python program there are a random list (which elements are unique, and which elements' number and values of interval are given by user), and a function which orders the list's numbers using the gnome sort

import random

stp = [] #empty list

jk = int(input("How many numbers has the list? ")) #elements' number is given by user
print(jk)
a = int(input("Choose the minimum value of an interval: ")) # this value is given by user
print(a)
b = int(input("Choose the maximum value of an interval: ")) # this value is given by user
print(b)

for j in range(jk): #this is a for cycle
    num = random.randint(a,b) #this instruction puts integer numbers between a and b
    if num not in stp: #not repeating number
       stp.append(num)
       j += 1

print("The random list is",stp)

def gnomesort(stp):
    if len(stp) <= 1:
        return stp #if the list's length is less than 1, or if it's as equal as 1, the list won't be ordered
    i = 1
    
    while i < len(stp):
          if stp[i-1]<=stp[i]: #if stp[i-1] is less than stp[i], or if they are equal, the index will move forward by one step
             i +=1
          else:
             stp[i-1], stp[i] = stp[i], stp[i-1]
             i -= 1 #the index moves backward by one step
             if(i == 0):
                i = 1
    return "Now the list is ordered with gnome sort", stp       

print(gnomesort(stp))
