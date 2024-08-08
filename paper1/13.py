n = int(input("Enter the number: "))
a, b = 0, 1
print("Fibonacci seres:")
for c in range(n):
    print(a, end=" ")
    a, b = b, a + b