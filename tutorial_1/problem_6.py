data_base: list[dict[str, str]] = []
exit_condition = False


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
   3. Search Record(s)
   4. Modify Record
   5. Delete Record
   6. Exit
"""
    )
    return int(input("Your choice [1-4]: "))


def format_str(input_str: str, length: int) -> str:
    return input_str + (length - len(input_str)) * " "


def print_all_data():
    print("NO    ID           Name              DOB        Height    Weight")
    for student_idx in range(len(data_base)):
        student_info = data_base[student_idx]
        number = format_str(str(student_idx), 6)
        student_id = format_str(student_info["ID"], 13)
        student_name = format_str(student_info["name"], 18)
        date_of_birth = format_str(student_info["date_of_birth"], 11)
        student_height = format_str(student_info["height"], 10)
        student_weight = student_info["weight"]
        print(number + student_id + student_name + date_of_birth + student_height + student_weight)


def search_students():
    print("* Enter search criteria")
    query_id = input("Student ID:").strip()
    query_name = input("Name:").strip()
    query_date_of_birth = input("Date of Birth:").strip()
    query_height = input("Height:").strip()
    query_weight = input("Weight:").strip()

    id_match = [data_base.index(student) for student in data_base if query_id in student["ID"]] if len(query_id) > 0 else []
    name_match = [data_base.index(student) for student in data_base if query_name in student["name"]] if len(query_name) > 0 else []
    date_of_birth_match = [data_base.index(student) for student in data_base if query_date_of_birth in student["date_of_birth"]] if len(query_date_of_birth) > 0 else []
    height_match = [data_base.index(student) for student in data_base if query_height in student["height"]] if len(query_height) > 0 else []
    weight_match = [data_base.index(student) for student in data_base if query_weight in student["weight"]] if len(query_weight) > 0 else []

    match_set = list(set(id_match + name_match + date_of_birth_match + height_match + weight_match))
    match_set.sort()
    if len(match_set) == 0:
        return print("No students fit the given criteria")
    print("NO    ID           Name              DOB        Height    Weight")
    for idx in match_set:
        student_info = data_base[idx]
        number = format_str(str(idx + 1), 6)
        student_id = format_str(student_info["ID"], 13)
        student_name = format_str(student_info["name"], 18)
        date_of_birth = format_str(student_info["date_of_birth"], 11)
        student_height = format_str(student_info["height"], 10)
        student_weight = student_info["weight"]
        print(number + student_id + student_name + date_of_birth + student_height + student_weight)
    return match_set


def modify_data():
    filtered_students = search_students()
    if len(filtered_students) == 0:
        return
    if len(filtered_students) > 1:
        print("More than 1 record is selected")
        return
    else:
        id = input("Student ID:").strip()
        name = input("Name:").strip()
        date_of_birth = input("Date of Birth:").strip()
        height = input("Height:").strip()
        weight = input("Weight:").strip()
        data_base[filtered_students[0]] = {
            "ID": id if len(id) else filtered_students[0]["ID"],
            "name": name if len(name) else filtered_students[0]["name"],
            "date_of_birth": date_of_birth if len(date_of_birth) else filtered_students[0]["date_of_birth"],
            "height": height if len(height) else filtered_students[0]["height"],
            "weight": weight if len(weight) else filtered_students[0]["weight"],
        }


def delete_data():
    filtered_students = search_students()
    if len(filtered_students) == 0:
        return
    if len(filtered_students) > 1:
        print("More than 1 record is selected")
        return
    else:
        data_base.pop(filtered_students[0])


while not exit_condition:
    idx = welcome_screen()
    if idx == 1:
        data_base.append(input_student_data())
    if idx == 2:
        print_all_data()
    if idx == 3:
        search_students()
    if idx == 6:
        exit_condition = True
