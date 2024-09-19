def fibonacii(n):
    if n>=1:
        n1,n2=0,1 
        
    for i in range(1,n+1):
            print(n1)
            n1,n2=n2,n1+n2
                      
n=int(input("Enter the number:"))
print("The numbers are,")
fibonacii(n)