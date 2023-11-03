def input_student_data() -> dict[str, str]:
    student_id = input("Please input your Student ID:")
    student_name = input("Please input your name:")
    date_of_birth = input("Please input your Date of Birth:")
    student_height = input("Please input your height:")
    student_weight = input("Please input your weight:")
    return {
        "ID": student_id,
        "name": student_name,
        "date_of_birth": date_of_birth,
        "height": student_height,
        "weight": student_weight,
    }


def welcome_screen() -> int:
    print(
        """
***Welcome to the Department of Electrical Engineering***
***              Student Database System              ***
   1. Enter New Record
   2. Print All Records
   3. Exit
"""
    )
    return int(input("Your choice [1-3]: "))


def format_str(input_str: str, length: int) -> str:
    return input_str + (length - len(input_str)) * " "


def print_data():
    print("NO    ID           Name              DOB        Height    Weight")
    for student_idx in range(len(data_base)):
        student_info = data_base[student_idx]
        number = format_str(str(student_idx + 1), 6)
        student_id = format_str(student_info["ID"], 13)
        student_name = format_str(student_info["name"], 18)
        date_of_birth = format_str(student_info["date_of_birth"], 11)
        student_height = format_str(student_info["height"], 10)
        student_weight = student_info["weight"]
        print(number + student_id + student_name + date_of_birth + student_height + student_weight)


data_base: list[dict[str, str]] = []
exit_condition = False

while not exit_condition:
    idx = welcome_screen()
    if idx == 1:
        data_base.append(input_student_data())
    if idx == 2:
        print_data()
    if idx == 3:
        exit_condition = True
