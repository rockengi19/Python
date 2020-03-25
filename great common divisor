# This Python code finds the great common divisor of two integer numbers with the Euclid's method

print("Research of the great common divisor")

m = int(input("Write the first number: "))
print(m)
n = int(input("Write the second number: "))
print(n)

def Euclid(m,n):
    if m*n == 0:
       return 1
    if m == n:
       return m
    elif m > n:
       return Euclid(m-n,n)
    else:
       return "The great common divisor of",m,"and",n,"is", Euclid(n-m,m)
            
print(Euclid(m,n))
