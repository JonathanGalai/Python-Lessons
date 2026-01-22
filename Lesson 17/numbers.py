def sum_even(num):
    total = 0
    for i in range(0, num + 1, 2):
        total += i
    return total


num = int(input("Choose a number:\n"))
result = sum_even(num)
print(result)