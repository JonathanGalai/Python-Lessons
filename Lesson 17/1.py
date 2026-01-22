def sum_numbers(num):
    sum = 0
    for i in range(num + 1):
        sum = sum + i
    return sum
num = int(input("Choose a number:\n"))
print(sum_numbers(num))