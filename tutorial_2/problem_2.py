from math import sqrt

print(
    """***Quadratic Equation Solver***
Please key in the following quadratic equation coefficients"""
)
a = float(input("a :"))
b = float(input("b :"))
c = float(input("c :"))
determinant = b**2 - 4 * a * c
if determinant > 0:
    print("The solutions for the quadratic equations are:")
    print(f"x1 = {(-b+sqrt(determinant))/(2*a)}")
    print(f"x2 = {(-b-sqrt(determinant))/(2*a)}")
if determinant == 0:
    print("The solution for the quadratic equations is:")
    print(f"x = {-b/(2*a)}")
if determinant < 0:
    print("The solutions for the quadratic equations are:")
    print(f"x1 = {(-b+sqrt(abs(determinant))*1j)/(2*a)}")
    print(f"x2 = {(-b-sqrt(abs(determinant))*1j)/(2*a)}")

("""*** End ***""")
