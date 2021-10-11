a = int(input("Enter the Numerator "))
b = int(input("Enter the Denominator "))
res = 0
try:
    res = a/b
    print(res)
except:
    print('Division by Zero not possible')
