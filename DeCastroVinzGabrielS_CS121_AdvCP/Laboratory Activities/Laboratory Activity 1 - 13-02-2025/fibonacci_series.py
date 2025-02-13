n = int(input("Enter the number of terms: "))

first = 0
second = 1

print("Fibonacci Sequence:", end=" ")

for count in range(n):
    print(first, end=" ")
    next = first + second
    first = second
    second = next


