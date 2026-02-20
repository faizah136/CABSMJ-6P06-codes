def avg_marks(marks):
    total=sum(marks)
    avg=total/len(marks)
    return avg

n=int(input("Enter number of subjects:"))
marks=[]
for i in range(n):
    mark=float(input("Enter marks:"))
    marks.append(mark)
avg=avg_marks(marks)
print("\nAverage of marks:", avg)

def celsius_to_fahrenheit(c):
    return (c*9/5)+32
c = float(input("Enter temperature in celsius:"))
f = celsius_to_fahrenheit(c)
print("Temperature in Fahrenheit:", f)

def rectangle_perimeter(length, breadth):
    if length<=0 or breadth<=0:
        print("invalid dimentions")
    return 2*(length+breadth)

l = float(input("Enter length (in cm):"))
b = float(input("Enter breadth (in cm):"))
p = rectangle_perimeter(l, b)
print(f"Perimeter of rectangle: {p} cm")
