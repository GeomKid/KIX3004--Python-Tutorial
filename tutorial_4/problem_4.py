input_str = input("Enter a string:")

splitted = input_str.split()
filtered = list(set([item.lower() for item in splitted]))

print(f"There are {len(splitted)} words.")
if len(splitted) > 0:
    print("The occurences of each words are:")

    for item in filtered:
        print(f"{item}:{splitted.count(item)}")
