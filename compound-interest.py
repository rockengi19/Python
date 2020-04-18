# This code uses a compound interest formula to calculate the addition between the sum of a loan (or deposit) and its interest 

t = int(input("Choose the number of years: "))
print(t)
p = float(input("Write the initial value of your loan/deposit: "))
print("EUR",p)
n = 15
i = float(input("Write the tax on interest: "))
print(i)
a = p*(1 + (i/n))**(n*t)
print("The final value is EUR",round(a,2))
