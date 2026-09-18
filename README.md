# Assignment 1 – Mini Project

## Console-Based Record Management Application Using Python

### Project Name

**Student Record Management System**

---

## Project Description

The **Student Record Management System** is a console-based, menu-driven application developed using Python. It allows users to manage student records through a simple text-based interface.

The application provides basic record-management operations such as **adding, viewing, searching, updating, and deleting** student records. Student information is stored in a JSON file so that the records remain available even after the application is closed and restarted.

This project demonstrates the use of fundamental Python programming concepts including variables, data types, conditional statements, loops, functions, exception handling, File I/O, JSON, input validation, and CRUD operations.

---

## Features

* Add Student Record
* View All Student Records
* Search Student by Student ID
* Update Student Record
* Delete Student Record with confirmation
* Input validation
* Exception handling
* Menu-driven console interface
* JSON file storage
* Data persistence after restarting the application
* Separate functions for different record-management operations

---

## Technologies Used

* **Programming Language:** Python
* **Data Storage:** JSON
* **Development Environment:** Visual Studio Code
* **Version Control and Repository:** GitHub

---

## Python Concepts Used

The application integrates the following Python concepts:

* Variables
* Data Types
* Lists
* Dictionaries
* Conditional Statements
* Loops
* Functions
* Exception Handling
* File I/O
* JSON
* String Handling
* Input Validation
* Menu-Driven Console Application Design
* CRUD Operations

---

## CRUD Operations

| Operation | Function Used                        |
| --------- | ------------------------------------ |
| Create    | `add_record()`                       |
| Read      | `view_records()` / `search_record()` |
| Update    | `update_record()`                    |
| Delete    | `delete_record()`                    |

---

## Project Files

| File / Folder               | Description                                                |
| --------------------------- | ---------------------------------------------------------- |
| `student_record_manager.py` | Main Python source code containing the application         |
| `students.json`             | Stores student records in JSON format                      |
| `Assignment1.pdf`           | Complete assignment documentation                          |
| `screenshots/`              | Contains screenshots demonstrating the working application |
| `README.md`                 | Project description, features, concepts, and instructions  |

---

## How to Run the Application

### Step 1: Open the Project

Download or clone this repository and open the project folder in **Visual Studio Code** or another Python-supported editor.

### Step 2: Open the Terminal

Open the terminal or command prompt and navigate to the project folder.

### Step 3: Run the Python Application

Use the following command:

```bash
python student_record_manager.py
```

### Step 4: Use the Menu

After running the program, the following menu is displayed:

```text
========================================
   STUDENT RECORD MANAGEMENT SYSTEM
========================================

1. Add Student Record
2. View All Records
3. Search Student
4. Update Student Record
5. Delete Student Record
6. Exit Application

Enter your choice (1-6):
```

Enter the required menu number and follow the instructions displayed by the application.

---

## Sample Input / Output

### Add Student Record

```text
Enter Student ID: 101
Enter Name: Sara Wadke
Enter Age: 20
Enter Course: MCA
Enter Email: sarawadke2018@example.com
Enter Percentage: 95

Student record added successfully.
```

### View All Records

```text
Student ID : 101
Name       : Sara Wadke
Age        : 20
Course     : MCA
Email      : sarawadke2018@example.com
Percentage : 95
```

### Search Student

```text
Enter Student ID to search: 101

Student record found.
```

### Update Student Record

```text
Enter Student ID to update: 101

Student record updated successfully.
```

### Delete Student Record

```text
Enter Student ID to delete: 101
Are you sure you want to delete this record? (yes/no): yes

Student record deleted successfully.
```

---

## Data Storage and Persistence

Student records are stored in the `students.json` file.

The application loads existing records from the JSON file when it starts. Whenever a record is added, updated, or deleted, the changes are saved back to the file.

This allows the records to remain available even after the application is closed and started again.

---

## Exception Handling and Input Validation

The application uses exception handling and input validation to handle common errors and invalid user inputs.

Examples include:

* Invalid age input
* Age outside the allowed range
* Invalid percentage input
* Percentage outside the range of 0 to 100
* Empty required fields
* Duplicate Student ID
* Invalid menu choice
* Missing JSON file
* Invalid JSON data
* File-related errors

Python `try-except` blocks are used to handle input and file-related exceptions without causing the application to stop unexpectedly.

---

## Application Workflow

The application follows this basic workflow:

1. The application starts.
2. Existing records are loaded from `students.json`.
3. The main menu is displayed.
4. The user selects an operation from the menu.
5. The selected record-management operation is performed.
6. Changes are saved to the JSON file where required.
7. The main menu is displayed again.
8. The user can perform another operation or select **Exit Application**.

---

## Screenshots

The `screenshots/` folder contains screenshots demonstrating the working of the application.

The screenshots include:

1. Main Menu
2. Add Student Record
3. Main Menu - After Adding Records
4. View All Records
5. Search Student
6. Update Student Record
7. Delete Student Record
8. Exception Handling – Invalid Input
9. File Persistence – Records Retained After Restarting
10. JSON File Storage – Stored Student Records

---

## Testing

The application was tested for the following operations:

| Test Case                      | Result            |
| ------------------------------ | ----------------- |
| Add valid student record       | Passed            |
| View all records               | Passed            |
| Search existing student        | Passed            |
| Update existing student        | Passed            |
| Delete student record          | Passed            |
| Invalid age input              | Handled correctly |
| Invalid percentage input       | Handled correctly |
| Invalid menu choice            | Handled correctly |
| Data persistence after restart | Passed            |

---

## Documentation

The complete assignment documentation is available in:

**`Assignment1.pdf`**

The report includes the project introduction, objectives, features, Python concepts used, files used, application workflow, exception handling and validation, working screenshots, testing, conclusion, and GitHub repository details.

---

## Repository Structure

```text
Assignment_1_Console_Record_Management_Application/
│
├── student_record_manager.py
├── students.json
├── README.md
├── Assignment1.pdf
│
└── screenshots/
    ├── 1_main_menu.png
    ├── 2_add_record.png 
    ├── 3_main_menu(After adding ).png
    ├── 4_view_records.png
    ├── 5_search_records.png
    ├── 6_update_records.png
    ├── 7_delete_records.png
    ├── 8_exception_handling.png
    ├── 9_file_persistence.png
    └── 10_json_file_storage.png
```

---

## Author

**Name:** Sara Sachin Wadke
**Roll No.:** 41

## Assignment

**Assignment 1 – Mini Project**

**Subject:** Python Programming & Relational Database

**Project:** Student Record Management System

---

## GitHub Repository

This repository contains the complete project source code, JSON data file, README documentation, assignment report, and screenshots.

**Repository:**
`https://github.com/sara-wadke/Assignment_1_Console_Record_Management_Application`

