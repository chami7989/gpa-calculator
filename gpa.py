def calculate_gpa():
    num_subjects = int(input("Enter the number of subjects: "))
    total_credits = 0
    total_grade_points = 0

    for i in range(num_subjects):
        subject_name = input(f"Enter the name of subject {i + 1}: ")
        credit_hours = int(input(f"Enter the credit hours for {subject_name}: "))
        grade = input(f"Enter the grade for {subject_name} (A, A-, B+, etc.): ")

        # Convert the grade to a numeric value (you can extend this as needed)
        grade_points = 0
        if grade == 'A+':
            grade_points = 4.2
        elif grade == 'A':
            grade_points = 4.0
        elif grade == 'A-':
            grade_points = 3.7
        elif grade == 'B+':
            grade_points = 3.3
        elif grade == 'B':
            grade_points = 3.0
        elif grade == 'B-':
            grade_points = 2.7
        elif grade == 'C+':
            grade_points = 2.3
        elif grade == 'C':
            grade_points = 2.0
        elif grade == 'C-':
            grade_points = 1.5
        elif grade == 'D':
            grade_points = 1.0
        elif grade == 'IWE':
            grade_points = 0.0

            
        # Add more grade-point mappings as necessary

        total_credits += credit_hours
        total_grade_points += grade_points * credit_hours

    if total_credits == 0:
        gpa = 0.0
    else:
        gpa = total_grade_points / total_credits

    print(f"Your GPA for this semester is: {gpa:.2f}")

calculate_gpa()
