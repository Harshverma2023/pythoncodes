
A = int(input("Enter a number: "))
odd = 0
for i in range(1, A+1):
    if i % 2 != 0:   
        odd+= i

print("Sum of odd numbers from 1 to", A, "is:", odd)
