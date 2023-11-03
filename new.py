from tkinter import Tk, Label, Entry, Button

def calculate_gpa():
    num_subjects = int(subjects_entry.get())
    total_credits = 0
    total_grade_points = 0

    for i in range(num_subjects):
        subject_name = subject_name_entries[i].get()
        credit_hours = int(credit_hour_entries[i].get())
        grade = grade_entries[i].get()

        # GPA calculation logic goes here
        # You can use the selected_grade and selected_credit_hours in your calculation

        # For demonstration purposes, let's just display the selected grade and credit hours
        result_label.config(text=f"Subject {i + 1}: {subject_name}, Credits: {credit_hours}, Grade: {grade}")

root = Tk()
root.title("GPA Calculator")

Label(root, text="Enter the number of subjects:").pack()
subjects_entry = Entry(root)
subjects_entry.pack()

subject_name_entries = []
credit_hour_entries = []
grade_entries = []

Button(root, text="Enter Subject Info", command=lambda: create_subject_entries()).pack()

result_label = Label(root, text="")
result_label.pack()

def create_subject_entries():
    num_subjects = int(subjects_entry.get())
    
    for i in range(num_subjects):
        Label(root, text=f"Subject {i + 1}:").pack()
        subject_name_entry = Entry(root)
        credit_hour_entry = Entry(root)
        grade_entry = Entry(root)
        subject_name_entry.pack()
        credit_hour_entry.pack()
        grade_entry.pack()
        subject_name_entries.append(subject_name_entry)
        credit_hour_entries.append(credit_hour_entry)
        grade_entries.append(grade_entry)

Button(root, text="Calculate GPA", command=calculate_gpa).pack()

root.mainloop()
