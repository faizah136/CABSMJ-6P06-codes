l = int(input("Enter the length of the cuboid (in cm): "))
b = int(input("Enter the breadth of the cuboid (in cm): "))
h = int(input("Enter the height of the cuboid (in cm): "))

area = 2*(l*b + b*h + l*h)
volume = l*b*h
print(f"Surface area of the cuboid = {area} cm^2")
print(f"Volume of the cuboid = {volume} cm^3")
