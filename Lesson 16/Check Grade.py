def check_grade(grade):
    if grade > 90:
        print("Exellent Grade!")
    elif grade > 60:
        print("Good")
    else:
        print("Failed")

while True:
    grade = int(input("Enter grade:\n"))
    if grade > 60:
        check_grade(grade)
    else:
        break