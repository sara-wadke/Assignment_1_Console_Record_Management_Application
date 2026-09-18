import json


# ============================================================
# FILE CONFIGURATION
# ============================================================

FILE_NAME = "students.json"


# ============================================================
# DISPLAY FUNCTIONS
# ============================================================

def print_header(title):
    """Display a formatted section heading."""
    print("\n" + "=" * 60)
    print(f"{title:^60}")
    print("=" * 60)


def pause():
    """Pause the program until the user is ready to continue."""
    input("\nPress Enter to continue...")


# ============================================================
# FILE I/O FUNCTIONS
# ============================================================

def load_records():
    """
    Load student records from the JSON file.
    Demonstrates File I/O and Exception Handling.
    """
    try:
        with open(FILE_NAME, "r") as file:
            records = json.load(file)

            # Make sure the JSON contains a list
            if isinstance(records, list):
                return records

            print("\n[ERROR] Invalid data format in students.json.")
            return []

    except FileNotFoundError:
        # If the file does not exist, start with an empty list.
        return []

    except json.JSONDecodeError:
        print("\n[ERROR] Unable to read students.json.")
        print("[INFO] The file contains invalid JSON data.")
        return []

    except OSError:
        print("\n[ERROR] A file-related error occurred.")
        return []


def save_records(records):
    """
    Save student records to the JSON file.
    Demonstrates File I/O and Exception Handling.
    """
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(records, file, indent=4)

        return True

    except OSError:
        print("\n[ERROR] Unable to save records to the file.")
        return False


# ============================================================
# INPUT VALIDATION FUNCTIONS
# ============================================================

def get_valid_age():
    """Get a valid integer age from the user."""
    while True:
        try:
            age = int(input("  Age              : "))

            if age <= 0:
                print("  [ERROR] Age must be greater than 0.")
            elif age > 100:
                print("  [ERROR] Please enter a valid age.")
            else:
                return age

        except ValueError:
            print("  [ERROR] Age must be a whole number.")


def get_valid_percentage():
    """Get a valid percentage between 0 and 100."""
    while True:
        try:
            percentage = float(input("  Percentage       : "))

            if percentage < 0 or percentage > 100:
                print("  [ERROR] Percentage must be between 0 and 100.")
            else:
                return percentage

        except ValueError:
            print("  [ERROR] Percentage must be a number.")


def get_non_empty_input(message):
    """Get non-empty text input from the user."""
    while True:
        value = input(message).strip()

        if value == "":
            print("  [ERROR] This field cannot be empty.")
        else:
            return value


# ============================================================
# ADD RECORD
# ============================================================

def add_record(records):
    """Add a new student record."""

    print_header("ADD STUDENT RECORD")

    student_id = get_non_empty_input("  Student ID       : ")

    # Check whether the Student ID already exists.
    for student in records:
        if student["student_id"] == student_id:
            print("\n  [ERROR] Student ID already exists.")
            pause()
            return

    name = get_non_empty_input("  Student Name     : ")
    age = get_valid_age()
    course = get_non_empty_input("  Course           : ")
    email = get_non_empty_input("  Email            : ")
    percentage = get_valid_percentage()

    # Dictionary stores one student's information.
    student = {
        "student_id": student_id,
        "name": name,
        "age": age,
        "course": course,
        "email": email,
        "percentage": percentage
    }

    # Add the dictionary to the list of records.
    records.append(student)

    if save_records(records):
        print("\n" + "-" * 60)
        print("  [SUCCESS] Student record added successfully.")
        print("-" * 60)

    pause()


# ============================================================
# VIEW RECORDS
# ============================================================

def view_records(records):
    """Display all student records."""

    print_header("VIEW ALL STUDENT RECORDS")

    if len(records) == 0:
        print("\n  [INFO] No student records found.")
        pause()
        return

    print(f"\n  Total Records: {len(records)}")

    for number, student in enumerate(records, start=1):
        print("\n" + "-" * 60)
        print(f"  Record {number}")
        print("-" * 60)

        print(f"  Student ID       : {student['student_id']}")
        print(f"  Student Name     : {student['name']}")
        print(f"  Age              : {student['age']}")
        print(f"  Course           : {student['course']}")
        print(f"  Email            : {student['email']}")
        print(f"  Percentage       : {student['percentage']:.2f}%")

    print("\n" + "-" * 60)
    pause()


# ============================================================
# SEARCH RECORD
# ============================================================

def search_record(records):
    """Search for a student record using Student ID."""

    print_header("SEARCH STUDENT")

    if len(records) == 0:
        print("\n  [INFO] No student records available.")
        pause()
        return

    student_id = get_non_empty_input("  Enter Student ID : ")

    found = False

    # Search through the list using a loop.
    for student in records:
        if student["student_id"] == student_id:
            found = True

            print("\n" + "-" * 60)
            print("                  STUDENT DETAILS")
            print("-" * 60)

            print(f"  Student ID       : {student['student_id']}")
            print(f"  Student Name     : {student['name']}")
            print(f"  Age              : {student['age']}")
            print(f"  Course           : {student['course']}")
            print(f"  Email            : {student['email']}")
            print(f"  Percentage       : {student['percentage']:.2f}%")

            print("-" * 60)
            break

    if not found:
        print("\n" + "-" * 60)
        print("  [INFO] No student found with this Student ID.")
        print("-" * 60)

    pause()


# ============================================================
# UPDATE RECORD
# ============================================================

def update_record(records):
    """Update an existing student record."""

    print_header("UPDATE STUDENT RECORD")

    if len(records) == 0:
        print("\n  [INFO] No student records available.")
        pause()
        return

    student_id = get_non_empty_input("  Enter Student ID : ")

    found = False

    for student in records:
        if student["student_id"] == student_id:
            found = True

            print("\n  Current Record")
            print("  " + "-" * 54)
            print(f"  Name             : {student['name']}")
            print(f"  Age              : {student['age']}")
            print(f"  Course           : {student['course']}")
            print(f"  Email            : {student['email']}")
            print(f"  Percentage       : {student['percentage']:.2f}%")
            print("  " + "-" * 54)

            print("\n  Enter the new details:")

            student["name"] = get_non_empty_input("  Student Name     : ")
            student["age"] = get_valid_age()
            student["course"] = get_non_empty_input("  Course           : ")
            student["email"] = get_non_empty_input("  Email            : ")
            student["percentage"] = get_valid_percentage()

            if save_records(records):
                print("\n" + "-" * 60)
                print("  [SUCCESS] Student record updated successfully.")
                print("-" * 60)

            break

    if not found:
        print("\n" + "-" * 60)
        print("  [INFO] Student ID not found.")
        print("-" * 60)

    pause()


# ============================================================
# DELETE RECORD
# ============================================================

def delete_record(records):
    """Delete a student record using Student ID."""

    print_header("DELETE STUDENT RECORD")

    if len(records) == 0:
        print("\n  [INFO] No student records available.")
        pause()
        return

    student_id = get_non_empty_input("  Enter Student ID : ")

    found = False

    for student in records:
        if student["student_id"] == student_id:
            found = True

            print("\n" + "-" * 60)
            print(f"  Student Name     : {student['name']}")
            print(f"  Student ID       : {student['student_id']}")
            print("-" * 60)

            confirmation = input(
                "  Are you sure you want to delete this record? (y/n): "
            ).strip().lower()

            if confirmation == "y":
                records.remove(student)

                if save_records(records):
                    print("\n" + "-" * 60)
                    print("  [SUCCESS] Student record deleted successfully.")
                    print("-" * 60)

            elif confirmation == "n":
                print("\n  [INFO] Delete operation cancelled.")

            else:
                print("\n  [ERROR] Invalid confirmation. Record was not deleted.")

            break

    if not found:
        print("\n" + "-" * 60)
        print("  [INFO] Student ID not found.")
        print("-" * 60)

    pause()


# ============================================================
# MAIN MENU
# ============================================================

def display_menu(records):
    """Display the main menu."""

    print("\n" + "=" * 60)
    print("             STUDENT RECORD MANAGEMENT SYSTEM")
    print("=" * 60)

    print("\n                       MAIN MENU")
    print("-" * 60)

    print("  1. Add Student Record")
    print("  2. View All Records")
    print("  3. Search Student")
    print("  4. Update Student Record")
    print("  5. Delete Student Record")
    print("  6. Exit Application")

    print("\n" + "-" * 60)
    print(f"  Total Records: {len(records)}")
    print("-" * 60)


# ============================================================
# MAIN FUNCTION
# ============================================================

def main():
    """
    Main program function.
    Demonstrates menu-driven application design,
    loops and conditional statements.
    """

    # Load existing records when the application starts.
    records = load_records()

    while True:
        display_menu(records)

        choice = input("\n  Enter your choice (1-6): ").strip()

        # Conditional statements control the menu operations.
        if choice == "1":
            add_record(records)

        elif choice == "2":
            view_records(records)

        elif choice == "3":
            search_record(records)

        elif choice == "4":
            update_record(records)

        elif choice == "5":
            delete_record(records)

        elif choice == "6":
            print("\n" + "=" * 60)
            print("       Thank you for using Student Record System!")
            print("=" * 60)
            print()
            break

        else:
            print("\n" + "-" * 60)
            print("  [ERROR] Invalid choice.")
            print("  Please enter a number from 1 to 6.")
            print("-" * 60)


# ============================================================
# PROGRAM EXECUTION
# ============================================================

if __name__ == "__main__":
    main()