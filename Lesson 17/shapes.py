def area(shape):
    if shape == 'circle':
        radius = float(input("Enter the radius of the circle:\n"))
        return radius * radius * 3.14

    elif shape == 'square':
        edge_length = float(input("Enter the edge length of the square:\n"))
        return edge_length * edge_length

    elif shape == 'triangle':
        base_length = float(input("Enter the base length of the triangle:\n"))
        height_length = float(input("Enter the height length of the triangle:\n"))
        return base_length * height_length // 2

    else:
        return 0


choose = int(input("Choose a shape:\n1 = circle\n2 = square\n3 = triangle\n"))

if choose == 1:
    print(area('circle'))

elif choose == 2:
    print(area('square'))

elif choose == 3:
    print(area('triangle'))

else:
    print("You didn't choose any of the options.")
