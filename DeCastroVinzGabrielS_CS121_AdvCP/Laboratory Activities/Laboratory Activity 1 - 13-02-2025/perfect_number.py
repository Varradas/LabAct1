num1 = int(input("Enter a number: "))
numlist = []

for count in range(num1):
    num2 = num1 / (count+1)
    if num2 % 1 == 0:
        numlist.append(num2)
     
numlistsum = sum(numlist) 

if numlistsum == (num1 + num1):
    print(f"{num1} is a perfect number.")
else:
    print(f"{num1} is not a perfect number.")
