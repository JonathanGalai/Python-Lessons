import random
lottery_ticket = random.randint(1, 100)
count = 0
number = int(input("Enter the lottery number from 1-100:\n"))
while lottery_ticket != number:
    lottery_ticket = random.randint(1, 100)
    count = count +1
print(count)
if count < 10:
    print("Your number is 10% rare")
else:
    print("Your number isn't rare")