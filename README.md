# Student Profile Management System

A beginner-friendly Python console project created to understand and practice the fundamentals of Python programming.

This project focuses mainly on **basic Python concepts**, including data types, variables, lists, dictionaries, list methods, user input, conditional statements, and nested `if` statements.

---

## About the Project

The **Student Profile Management System** collects basic information about a student and performs simple academic calculations.

The program takes the following information from the user:

* Student name
* Age
* Course
* Three skills
* Three marks

After collecting the information, the program displays the student profile and performs different calculations and checks.

---

## Courses Included

The program currently accepts the following courses:

* BCA
* BCOM
* BTECH
* BSC
* BE

---

## Features

The program performs the following operations:

* Takes student name as input
* Validates the student's age
* Accepts a valid course
* Takes three skills from the user
* Takes three marks from the user
* Validates marks between 0 and 100
* Displays the student profile
* Displays each skill with its corresponding mark
* Calculates total marks
* Calculates average marks
* Finds the highest mark
* Finds the lowest mark
* Determines the student's grade
* Determines PASS or FAIL
* Checks scholarship eligibility

---

## Python Concepts Practiced

This project was built mainly to understand the fundamentals of Python.

### 1. Variables

Used variables to store values such as:

```python
name
age
course
marks
marks2
marks3
avg
totalmarks
```

### 2. Data Types

The project uses basic Python data types such as:

* String (`str`)
* Integer (`int`)
* Float (`float`)
* List (`list`)
* Dictionary (`dict`)

Example:

```python
age = 21
course = "BCA"
avg = 86.67
```

### 3. Dictionaries

A dictionary is used to store the student's profile information.

```python
student = {
    'name': '',
    'age': '',
    'course': '',
    'skills': [],
    'marks': []
}
```

### 4. Lists

Lists are used to store multiple skills and marks.

Example:

```python
student['skills'] = ['PYTHON', 'SQL', 'HTML']
student['marks'] = [80, 90, 90]
```

### 5. List Indexing

The project uses indexing to access individual elements from a list.

```python
student['skills'][0]
student['marks'][0]
```

For example:

```text
student['skills'][0] → PYTHON
student['marks'][0]  → 80
```

### 6. List Method - `append()`

The `append()` method is used to add skills and marks to the lists.

```python
student['skills'].append("PYTHON")
student['marks'].append(80)
```

### 7. User Input

The `input()` function is used to collect information from the user.

```python
name = input("Enter the name of student: ")
```

### 8. Type Conversion

The `int()` function is used to convert input into an integer.

```python
age = int(input("Enter the age: "))
```

### 9. If, Elif and Else

The project uses conditional statements for validation and decision-making.

```python
if age <= 17:
    print("Age is invalid")
elif age >= 18 and age <= 25:
    print("Valid age")
else:
    print("Invalid age")
```

### 10. Nested If Statements

Nested `if` statements are used to practice conditions inside other conditions.

For example, scholarship eligibility checks:

```python
if avg >= 85:
    if marks >= 75:
        if marks2 >= 75:
            if marks3 >= 75:
                print("SCHOLARSHIP ELIGIBLE")
```

---

## How the Program Works

The program follows these basic steps:

```text
Start
  ↓
Enter student name
  ↓
Enter age
  ↓
Validate age
  ↓
Enter course
  ↓
Validate course
  ↓
Enter three skills
  ↓
Enter three marks
  ↓
Validate marks
  ↓
Display student profile
  ↓
Display skills and marks
  ↓
Calculate total and average
  ↓
Find highest and lowest marks
  ↓
Determine grade
  ↓
Determine PASS / FAIL
  ↓
Check scholarship eligibility
  ↓
End
```

---

## Example Input

```text
Enter the name of student: sss
Enter the age: 21
Enter a course: BCA
Enter skill 1: PYTHON
Enter skill 2: SQL
Enter skill 3: HTML
Enter marks 1: 80
Enter marks 2: 90
Enter marks 3: 90
```

---

## Example Output

```text
========= STUDENT PROFILE =========
NAME   : sss
AGE    : 21
COURSE : BCA

------------ MARKS SCORED ---------
PYTHON marks are : 80
SQL marks are : 90
HTML marks are : 90

------------- RESULT -------------
TOTAL MARKS   : 260
AVERAGE MARKS : 86.66666666666667
90 is highest
80 is lowest
Grade : A
RESULT : PASS
SCHOLARSHIP ELIGIBLE
```

---

## Grade System

The program determines the grade based on the average marks.

| Average  | Grade |
| -------- | ----- |
| 90 - 100 | A+    |
| 80 - 89  | A     |
| 70 - 79  | B+    |
| 60 - 69  | B     |
| 45 - 59  | C+    |
| 35 - 44  | C     |
| Below 35 | F     |

---

## Scholarship Eligibility

The student is considered eligible for the scholarship when:

* Average marks are **85 or above**
* Mark 1 is **75 or above**
* Mark 2 is **75 or above**
* Mark 3 is **75 or above**

The project uses nested `if` statements to practice this logic.

---

## Project Structure

```text
student_profile-python/
│
├── pystudent.py
└── README.md
```

---

## How to Run

### Step 1: Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/student_profile-python.git
```

### Step 2: Open the project folder

```bash
cd student_profile-python
```

### Step 3: Run the Python file

```bash
python pystudent.py
```

If your system uses `python3`:

```bash
python3 pystudent.py
```

---

## Technologies Used

* Python 3
* Git
* GitHub

---

## Purpose of the Project

This project was created as a **Python learning project** to understand basic programming concepts before moving toward more advanced Python topics.

The main focus was on understanding:

* Basic Python syntax
* Variables
* Data types
* User input
* Type conversion
* Lists
* Dictionaries
* List indexing
* Basic list methods
* `if`
* `elif`
* `else`
* Nested `if`
* Comparison operators
* Logical operators
* Arithmetic operations
* Basic problem-solving and conditional logic

---

## Future Improvements

As I continue learning Python, this project can be improved by adding:

* Functions to organize the code
* Loops
* Better input validation
* Multiple student records
* More subjects and skills
* File handling
* Exception handling
* SQLite database integration
* A menu-driven interface

---

## Author

**Sathwik**

BCA Graduate | Python & Data Analytics Learner

---

**Note:** This is a beginner-level learning project created to practice and understand Python fundamentals.
