print("*** Integer Input ***")
input_str = input("Please enter an integer:").strip()
while not input_str.isdigit():
    input_str = input("Error! Please enter an integer:").strip()
print("Integer entered is ", input_str, ".")
print("*** End ***")
