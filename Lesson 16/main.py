#print good morning
def print_good_morning():
    print("Good Morning Bro!!!")

print_good_morning()

#print name
def print_name(name):
    print(name + " is great!")

print_name("Galai")
print_name("Snir")

def check_grade(grade):
    if grade > 90:
        print("Exellent Grade!")
    elif grade > 80:
        print("Good")
    else:
        print("Talk to your teacher")

grade1 = 97
grade2 = 67
check_grade(grade1)
check_grade(grade2)
