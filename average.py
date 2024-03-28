students = {
    'Alice': [85, 90, 92],
    'Bob': [78, 82, 80],
    'Charlie': [95, 89, 92],
    'David': [70, 75, 72]
}

# Average grades per student:
average_grades = {
    student: sum(grades) / len(grades) for student, grades in students.items()
    }

print(average_grades)

# determine which student has the highest average grade by using the max function with a key argument 

student_with_highest_average = max(average_grades, key=average_grades.get) 
highest_average_grade = average_grades[student_with_highest_average]

print(f"The student with the highest average grade is {student_with_highest_average} with an average grade of {highest_average_grade}.")

#  Names of students whose average grade is above a certain threshold 
threshold = 85

above_threshold_students = [student for student, avg_grade in average_grades.items() if avg_grade > threshold]

print("Students with average grade above", threshold, ":")
for student in above_threshold_students:
    print(student)
