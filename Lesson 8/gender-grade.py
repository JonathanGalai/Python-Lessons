gender = input("What is your gender? write m or f:\n")

if gender == "m":
    grade1 = int(input("What is your Math grade?\n"))
    if grade1 >= 80:
        print("You were accepted")
    else:
        print("You were rejected")
if gender == "f":
    grade2 = int(input("What is your English grade?\n"))
    if grade2 >= 85:
        print("You were accepted")
    else:
        print("You were rejected")
