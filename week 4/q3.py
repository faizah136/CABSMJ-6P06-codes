from math import pi
def usable_area(R,r):
    return pi*(R**2-r**2)

R=float(input("Enter outer radius R(in cm):"))
r=float(input("Enter inner radius r(in cm):"))
if R<=0 or r<0:
    print("Invalid radius values.")
elif r>=R:
    print("Inner radius must be smaller than outer radius.")
else:
    area=usable_area(R,r)
    print(f"Effective usable area:{area: .5f} cm^2")
