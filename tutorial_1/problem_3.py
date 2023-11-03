from math import pi

print(
    """
Area Calculator for Basic Shapes
================================

    1. Square
    2. Rectangle
    3. Triangle
    4. Circle

"""
)
idx = int(input("Choose a shape [1-4] that you want to calculate : ").strip()) - 1


def square_calculate() -> None:
    side_length = float(input("Enter side length : "))
    print("Area of Square is ", side_length**2)


def rectangle_calculate() -> None:
    length = float(input("Enter length : "))
    base = float(input("Enter base : "))
    print("Area of Rectangle is ", length * base)


def triangle_calculate() -> None:
    height = float(input("Enter height : "))
    base = float(input("Enter base : "))
    print("Area of Triangle is ", 0.5 * height * base)


def circle_calculate() -> None:
    radius = float(input("Enter radius : "))
    print("Area of circle is ", round(pi * radius * radius, 2))


functions = [square_calculate, rectangle_calculate, triangle_calculate, circle_calculate]
functions[idx]()
