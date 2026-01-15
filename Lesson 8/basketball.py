continue_input = True
counter = 0
sum_baskets = 0

while continue_input:
    baskets = int(input("What is the number of baskets of the player? "))

    if baskets < 0:
        continue_input = False
        continue  # חוזרים ללולאה או יוצאים

    if baskets == 0:
        age = int(input("What is your age? "))
        if age < 20:
            continue  # לא סופרים את השחקן הזה
        # אם גיל >= 20, נמשיך ונספור אותו
    counter = counter + 1
    sum_baskets = sum_baskets + baskets

if counter > 0:
    print("Average baskets:", sum_baskets / counter)
else:
    print("No valid players to calculate average.")
