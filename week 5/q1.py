import math

def largest(a, b, c):
    if a >= b and a >= c:
        print("Largest number is:", a)
    elif b >= a and b >= c:
        print("Largest number is:", b)
    else:
        print("Largest number is:", c)


def volume():
    print("\nChoose shape:")
    print("1. Cylinder")
    print("2. Cube")
    print("3. Cuboid")

    choice = int(input("Enter shape choice: "))

    match choice:
        case 1: 
            r = float(input("Enter radius (in cm): "))
            h = float(input("Enter height (in cm): "))
            vol = math.pi * r * r * h
            print(f"Volume of Cylinder = {vol} cm^3")

        case 2:   
            a = float(input("Enter side (in cm): "))
            vol = a ** 3
            print(f"Volume of Cube = {vol} cm^3")

        case 3:  
            l = float(input("Enter length (in cm): "))
            w = float(input("Enter width (in cm): "))
            h = float(input("Enter height (in cm): "))
            vol = l * w * h
            print(f"Volume of Cuboid = {vol} cm^3")

        case _:
            print("Invalid shape choice")


def rectangle_area():
    l = float(input("Enter length (in cm): "))
    w = float(input("Enter width (in cm): "))
    area = l * w
    print(f"Area of Rectangle = {area} cm^2")


def circle_circumference():
    r = float(input("Enter radius (in cm): "))
    c = 2 * math.pi * r
    print(f"Circumference of Circle = {c} cm")


def swap_values():
    a = input("Enter first value: ")
    b = input("Enter second value: ")

    print("Before swapping: a =", a, " b =", b)

    a, b = b, a 

    print("After swapping: a =", a, " b =", b)


def distance_points():
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))

    d = math.dist((x1, y1), (x2, y2))
    print("Distance between points =", d)



while True:
    print("\n\tUtility Module")
    print("1. Largest of three numbers")
    print("2. Volume of shape")
    print("3. Area of rectangle")
    print("4. Circumference of circle")
    print("5. Swap two variables")
    print("6. Distance between two points")
    print("7. Exit")

    ch = int(input("Enter your choice: "))

    match ch:
        case 1:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            c = float(input("Enter third number: "))
            largest(a, b, c)

        case 2:
            volume()

        case 3:
            rectangle_area()

        case 4:
            circle_circumference()

        case 5:
            swap_values()

        case 6:
            distance_points()

        case 7:
            print("Exiting program.")
            break

        case _:
            print("Invalid choice")
