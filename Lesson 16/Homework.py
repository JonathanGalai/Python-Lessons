def three_numbers():
    number1 = int(input("Enter the first number:\n"))
    number2 = int(input("Enter the second number:\n"))
    number3 = int(input("Enter the third number:\n"))

    if number1 > number2 and number1 > number3:
        print(f"Number {number1} is the greatest")

    elif number2 > number1 and number2 > number3:
        print(f"Number {number2} is the greatest")

    else:
        print(f"Number {number3} is the greatest")

three_numbers()