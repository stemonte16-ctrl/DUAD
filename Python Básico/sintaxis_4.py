"""averages"""

note_counter = 1
number_of_passing_grades = 0
number_of_failed_grades = 0
sum_passing_grades = 0
sum_failing_grades = 0
overall_grade_sum = 0

total_grades = int(input("Enter the number of notes: "))

while note_counter <= total_grades:
    print("Enter the note number")
    current_note = int(input("Enter current note: "))
    
    if current_note < 70:
        number_of_failed_grades += 1
        sum_failing_grades += current_note
    else:
        number_of_passing_grades += 1
        sum_passing_grades += current_note
        
    overall_grade_sum += current_note
    note_counter += 1


if number_of_failed_grades > 0:
    average_of_failing_grades = sum_failing_grades / number_of_failed_grades
else:
    average_of_failing_grades = 0

if number_of_passing_grades > 0:
    average_of_passing_grades = sum_passing_grades / number_of_passing_grades
else:
    average_of_passing_grades = 0

if total_grades > 0:
    overall_grade_average = overall_grade_sum / total_grades
else:
    overall_grade_average = 0

print("The student has this many passing grades")
print(number_of_passing_grades)
print("This is the average of the passing grades")
print(average_of_passing_grades)
print("The student has this many failing grades")
print(number_of_failed_grades)
print("This is the average of the failing grades")
print(average_of_failing_grades)
print("This is the overall grade average")
print(overall_grade_average)
