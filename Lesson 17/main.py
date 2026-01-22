def diff(num1, num2):
    if num1 > num2:
        return num1 - num2
    else:
        return num2 - num1

num1 = int(input("Enter number 1:\n"))
num2 = int(input("Enter number 2:\n"))
result = diff(num1, num2)
print(result)
