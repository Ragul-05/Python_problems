def prime(num):
    for i in range(2,num):
        if (num<=2):
            return False
        if (num % i)==0:
            return False
    return True
n=int(input("Enter the number:"))
if prime(n):
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")
