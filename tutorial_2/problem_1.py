import numpy

print("***Complex Number in Polar Form ***")
complex_num = complex(input("Please enter a complex number: "))
magnitude = numpy.sqrt(complex_num.real**2 + complex_num.imag**2)
print(f"m = {magnitude}")
phase = numpy.arctan(complex_num.imag / complex_num.real) + (numpy.pi if complex_num.real < 0 else 0)
print(f"p = {phase}")
print("*** End ***")
