n=int(input("Enter a Number: "))
fact=1
if n==1 or n==0:
    print("factorial of ",n,"is",fact)
else:
    for i in range(1,n+1):
        fact=fact*i
print("Factorial of",n,"is",fact)

'''
num = int(input("Enter a number: "))    
factorial = 1    
if num < 0:    
 print(" Factorial does not exist for negative numbers")    
elif num == 0:    
	 print("The factorial of 0 is 1")    
else:    
 for i in range(1,num + 1):    
	factorial = factorial*i    
print("The factorial of",num,"is",factorial)'''
