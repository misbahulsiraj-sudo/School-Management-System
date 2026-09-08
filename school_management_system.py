# school_management_system.py

import json
import os

DATA_FILE = "school_data.json"


class SchoolManagementSystem:
    def __init__(self):
        self.students = self.load_data()

    def load_data(self):
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, "r") as file:
                    return json.load(file)
            except:
                pass
        return []

    def save_data(self):
        with open(DATA_FILE, "w") as file:
            json.dump(self.students, file, indent=4)

    def add_student(self):
        student_id = input("Student ID: ")
        name = input("Student Name: ")
        age = input("Age: ")
        grade = input("Class/Grade: ")

        for student in self.students:
            if student["id"] == student_id:
                print("Student ID already exists.")
                return

        self.students.append({
            "id": student_id,
            "name": name,
            "age": age,
            "class": grade,
            "marks": {}
        })

        self.save_data()
        print("Student added successfully.")

    def view_students(self):
        if not self.students:
            print("No students found.")
            return

        print("\n========== STUDENTS ==========")

        for student in self.students:
            print(
                f"ID: {student['id']} | "
                f"Name: {student['name']} | "
                f"Class: {student['class']}"
            )

    def search_student(self):
        student_id = input("Enter Student ID: ")

        for student in self.students:
            if student["id"] == student_id:

                print("\nStudent Found")
                print("-" * 30)

                print(f"ID    : {student['id']}")
                print(f"Name  : {student['name']}")
                print(f"Age   : {student['age']}")
                print(f"Class : {student['class']}")

                return

        print("Student not found.")

    def update_student(self):
        student_id = input("Student ID: ")

        for student in self.students:

            if student["id"] == student_id:

                student["name"] = input(
                    "New Name: "
                )

                student["age"] = input(
                    "New Age: "
                )

                student["class"] = input(
                    "New Class: "
                )

                self.save_data()

                print(
                    "Student updated successfully."
                )

                return

        print("Student not found.")

    def delete_student(self):
        student_id = input("Student ID: ")

        for student in self.students:

            if student["id"] == student_id:

                self.students.remove(student)

                self.save_data()

                print(
                    "Student deleted successfully."
                )

                return

        print("Student not found.")

    def add_marks(self):
        student_id = input("Student ID: ")

        for student in self.students:

            if student["id"] == student_id:

                subject = input("Subject: ")

                try:
                    marks = float(
                        input("Marks: ")
                    )

                    student["marks"][subject] = marks

                    self.save_data()

                    print(
                        "Marks added successfully."
                    )

                except ValueError:
                    print("Invalid marks.")

                return

        print("Student not found.")

    def calculate_grade(self, average):

        if average >= 90:
            return "A+"

        elif average >= 80:
            return "A"

        elif average >= 70:
            return "B"

        elif average >= 60:
            return "C"

        elif average >= 50:
            return "D"

        return "F"

    def report_card(self):
        student_id = input("Student ID: ")

        for student in self.students:

            if student["id"] == student_id:

                if not student["marks"]:
                    print(
                        "No marks available."
                    )
                    return

                print("\n")
                print("=" * 40)
                print("STUDENT REPORT CARD")
                print("=" * 40)

                print(
                    f"ID    : {student['id']}"
                )

                print(
                    f"Name  : {student['name']}"
                )

                print(
                    f"Class : {student['class']}"
                )

                print("\nSubjects:")

                total = 0

                for subject, marks in (
                    student["marks"].items()
                ):
                    print(
                        f"{subject}: {marks}"
                    )
                    total += marks

                average = (
                    total /
                    len(student["marks"])
                )

                grade = self.calculate_grade(
                    average
                )

                print("-" * 40)

                print(
                    f"Average: {average:.2f}"
                )

                print(
                    f"Grade  : {grade}"
                )

                print("=" * 40)

                return

        print("Student not found.")

    def statistics(self):
        total_students = len(
            self.students
        )

        print("\n========== STATISTICS ==========")

        print(
            f"Total Students: {total_students}"
        )

    def menu(self):

        while True:

            print("\n")
            print("=" * 50)
            print("SCHOOL MANAGEMENT SYSTEM")
            print("=" * 50)

            print("1. Add Student")
            print("2. View Students")
            print("3. Search Student")
            print("4. Update Student")
            print("5. Delete Student")
            print("6. Add Marks")
            print("7. Report Card")
            print("8. Statistics")
            print("9. Exit")

            choice = input(
                "\nEnter Choice: "
            )

            if choice == "1":
                self.add_student()

            elif choice == "2":
                self.view_students()

            elif choice == "3":
                self.search_student()

            elif choice == "4":
                self.update_student()

            elif choice == "5":
                self.delete_student()

            elif choice == "6":
                self.add_marks()

            elif choice == "7":
                self.report_card()

            elif choice == "8":
                self.statistics()

            elif choice == "9":
                self.save_data()
                print("Thank you!")
                break

            else:
                print("Invalid choice.")


if __name__ == "__main__":
    app = SchoolManagementSystem()
    app.menu()