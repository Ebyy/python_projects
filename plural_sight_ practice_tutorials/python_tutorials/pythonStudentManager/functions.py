students = []

def get_students_titlecase():
    students_titlecase = students
    for student in students:
        students_titlecase = student["name"].title()
    return students_titlecase

def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)

def add_student(name, student_id):
    student = {"name": name, "student_id": student_id}
    students.append(student)


while True:
    student_name = input("Please enter the name of the student: ")
    new_student_id = input("Please enter the the student ID number: ")
    continuation_prompt = input("\nWould you like to "
                                "enter another name? ")
    if continuation_prompt != "yes":
        break

add_student(name=student_name, student_id = new_student_id)
