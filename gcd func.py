def GCD(x,y):
    if x>y:
        small=y
    else:
        small=x
    for i in range(1,small+1):
        if((x%i==0)and(y%i==0)):
            gcd=i
    return gcd
n1=int(input("Enter a 1st number:"))
n2=int(input("Enter a 2nd number:"))
print("Gcd of ",n1,"and",n2,"is",GCD(n1,n2))
