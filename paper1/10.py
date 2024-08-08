num = int(input("enter the number for factorial:"))
print("num is",num)
factorial=1

for num in range(2,num+1):
   
    factorial *= num
    print("factorial of  no is",factorial)