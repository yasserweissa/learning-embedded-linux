import math

def calculate_circle_area(radius):
    area = math.pi * (radius ** 2)
    return area

radius = float(input("Enter the radius of the circle: "))
circle_area = calculate_circle_area(radius)
print(f"The area of the circle with radius {radius} is {circle_area:.2f}")

