def three_numbers():
    number1 = int(input("Enter the first number:\n"))
    number2 = int(input("Enter the second number:\n"))
    number3 = int(input("Enter the third number:\n"))

    if number1 > 10 and number2 > 10 and number3 > 10:
        print("All numbers are greater than 10")

    elif number1 < 10 and number2 < 10 and number3 > 10:
        print(number1 + number2)

    elif number1 < 10 and number2 > 10 and number3 < 10:
        print(number1 + number3)

    elif number1 > 10 and number2 < 10 and number3 < 10:
        print(number2 + number3)

    elif number1 < 10 and number2 < 10 and number3 < 10:
        print(number1 + number2 + number3)

    elif number1 < 10 and number2 > 10 and number3 > 10:
        print(number1)

    elif number1 > 10 and number2 < 10 and number3 > 10:
        print(number2)

    elif number1 > 10 and number2 > 10 and number3 < 10:
        print(number3)
three_numbers()