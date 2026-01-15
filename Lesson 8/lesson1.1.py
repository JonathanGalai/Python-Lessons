while True:
    num1 = int(input("\nWrite a number (Write 0 to end):\n"))
    num2 = int(input("Write a 2nd number:\n"))

    if num1 > num2:
        print(str(num1) + " is greater than " + str(num2))

    if num2 > num1:
        print(str(num2) + " is greater than " + str(num1))

    if num1 == num2:
        print(str(num1) + " is equal to " + str(num2))

    if num1 or num2 == 0:
        print("Goodbye!")
        break