students = []

def add_student(name, roll_no, email):
    if not name.strip():
        raise ValueError("Name cannot be empty")

    if not roll_no.strip():
        raise ValueError("Roll number cannot be empty")

    if "@" not in email or "." not in email.split("@")[-1]:
        raise ValueError("Invalid email")

    student = {
        "name": name,
        "roll_no": roll_no,
        "email": email
    }

    students.append(student)
    print("Student added successfully!")
    return student


def display_students():
    if not students:
        return "No students found."

    for student in students:
        print(student)


if __name__ == "__main__":
    add_student("Rahul", "101", "rahul@example.com")
    add_student("Priya", "102", "priya@example.com")

    print("Student Management System")
    display_students()
