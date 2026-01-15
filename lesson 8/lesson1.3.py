num1 = int(input("Write the 1st number:\n"))
num2 = int(input("Write the 2nd number:\n"))
num3 = int(input("Write the 3rd number:\n"))

if num1 >num2:
    if num1 > num3:
        print(str(num1) + " is the biggest")
    else:
        print(str(num3) + " is the biggest")
else:
    if num2 > num3:
        print(str(num2) + " is the biggest")
    else:
        print(str(num3) + " is the biggest")