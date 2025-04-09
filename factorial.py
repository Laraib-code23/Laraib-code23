def factorial(n):
    result =1
    for i in range(1, n+1):
        result *=i
    return result
num=int(input("Enter a number:"))
if num<0:
    print("Factorial not valid for negative number:")
else:
    print(f"The facorial of {num} is {factorial(num)}.")