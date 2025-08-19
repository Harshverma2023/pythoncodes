A = int(input("Enter base number: "))
B = int(input("Enter power: "))

result = 1
i = 1

while i <= B:
    result = result * A
    i = i + 1

print("Result =", result)
