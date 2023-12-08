import sys

try:
    float(sys.argv[2])
except ValueError:
    print("The value given is  not a number")

if "gramtopound" in sys.argv[1][1:].lower():
    print(f"{float(sys.argv[2])} gram is {float(sys.argv[2])*0.00220462}pound")
if "poundtogram" in sys.argv[1][1:].lower():
    print(f"{float(sys.argv[2])} pound is {float(sys.argv[2])/0.00220462} gram")
if "inchtometre" in sys.argv[1][1:].lower():
    print(f"{float(sys.argv[2])} inch is {float(sys.argv[2])/39.3701} metre")
if "metretoinch" in sys.argv[1][1:].lower():
    print(f"{float(sys.argv[2])} metre is {float(sys.argv[2])*39.3701} inch")
