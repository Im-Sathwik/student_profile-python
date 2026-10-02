# Student Profile and Marks Record
# Python Learning 


student = {
    'name': '',
    'age': '',
    'course': '',
    'skills': [],
    'marks': []
}


# ---------- STUDENT DETAILS ----------

student['name'] = input('Enter the name of student: ')

age = int(input('Enter the age: '))

if age <= 17:
    print('Age is invalid')

elif age >= 18 and age <= 25:
    print('Valid age')
    student['age'] = age

else:
    print('Invalid age')


# ---------- COURSE ----------

course = input('Enter a course(USE FORMAT - BCA,BE...): ')

if course == 'BCA':
    student['course'] = course

elif course == 'BCOM':
    student['course'] = course

elif course == 'BTECH':
    student['course'] = course

elif course == 'BSC':
    student['course'] = course

elif course == 'BE':
    student['course'] = course

else:
    print('Invalid course')


# ---------- SKILLS ----------

student['skills'].append(input("Enter skill 1: "))
student['skills'].append(input("Enter skill 2: "))
student['skills'].append(input("Enter skill 3: "))


# ---------- MARKS ----------

marks = int(input("Enter marks 1: "))

if marks >= 0 and marks <= 100:
    student['marks'].append(marks)
else:
    print('Invalid marks')


marks2 = int(input("Enter marks 2: "))

if marks2 >= 0 and marks2 <= 100:
    student['marks'].append(marks2)
else:
    print('Invalid marks')


marks3 = int(input("Enter marks 3: "))

if marks3 >= 0 and marks3 <= 100:
    student['marks'].append(marks3)
else:
    print('Invalid marks')


# ---------- STUDENT PROFILE ----------

print("\n========= STUDENT PROFILE =========")

print('NAME   :', student['name'])
print('AGE    :', student['age'])
print('COURSE :', student['course'])


# ---------- MARKS SCORED ----------

print('\n------------ MARKS SCORED ---------')

print(student['skills'][0], 'marks are :', student['marks'][0])
print(student['skills'][1], 'marks are :', student['marks'][1])
print(student['skills'][2], 'marks are :', student['marks'][2])


# ---------- RESULT ----------

print("\n------------- RESULT -------------")

totalmarks = marks + marks2 + marks3

print('TOTAL MARKS   :', totalmarks)

avg = totalmarks / 3

print('AVERAGE MARKS :', avg)


# ---------- HIGHEST MARK ----------

if marks > marks2:

    if marks > marks3:
        print(marks, "is highest")
    else:
        print(marks3, "is highest")

else:

    if marks2 > marks3:
        print(marks2, "is highest")
    else:
        print(marks3, "is highest")


# ---------- LOWEST MARK ----------

if marks < marks2:

    if marks < marks3:
        print(marks, "is lowest")
    else:
        print(marks3, "is lowest")

else:

    if marks2 < marks3:
        print(marks2, "is lowest")
    else:
        print(marks3, "is lowest")


# ---------- GRADE ----------

if avg >= 90 and avg <= 100:
    print("Grade : A+")

elif avg >= 80 and avg <= 89:
    print("Grade : A")

elif avg >= 70 and avg <= 79:
    print("Grade : B+")

elif avg >= 60 and avg <= 69:
    print("Grade : B")

elif avg >= 45 and avg <= 59:
    print("Grade : C+")

elif avg >= 35 and avg <= 44:
    print("Grade : C")

else:
    print("Grade : F")


# ---------- PASS / FAIL ----------

if marks <= 35:
    print("RESULT : FAIL")

elif marks2 <= 35:
    print("RESULT : FAIL")

elif marks3 <= 35:
    print("RESULT : FAIL")

else:
    print("RESULT : PASS")


# ---------- SCHOLARSHIP ELIGIBILITY ----------

if avg >= 85:

    if marks >= 75:

        if marks2 >= 75:

            if marks3 >= 75:
                print("SCHOLARSHIP ELIGIBLE")
            else:
                print("SCHOLARSHIP NOT ELIGIBLE")

        else:
            print("SCHOLARSHIP NOT ELIGIBLE")

    else:
        print("SCHOLARSHIP NOT ELIGIBLE")

else:
    print("SCHOLARSHIP NOT ELIGIBLE")
