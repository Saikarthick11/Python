a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
if(a>b):
    n=b
else:
    n=a
for i in range(1,n+1):
    if((a%i==0)and(b%i==0)):
        g=i
print("Gcd of ",a,"and",b,"is",g)        
