evens = []

n = int(input("How many integer numbers has your list? "))
print("There are",n,"integer numbers")

def alist(n):
    num = 0
    for i in range(n):
        num = int(input("Write a number: "))
        evens.append(num)
    return evens

print(alist(n))

def Even(evens):
    summa = 0
    for j in range(len(evens)):
        if evens[j]%2 == 0:
            summa += evens[j]
    return "This is the summa of the list's even numbers:", summa

print(Even(evens))
