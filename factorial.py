num=int(input("Enter the number : "))
i=1
result=1

while(i<=num):
    result*=i
    i+=1
    print("Factorial of number is :- ",result)



#using for loop

num=int(input("Enter the number : "))
re=1
for i in range(1,num+1):
    re*=i
    print("factorial of number is :- ",re)
"""
result = 1
for i in range(1, num + 1):
    result *= i
print("The factorial of {num} is {result}",re)"""