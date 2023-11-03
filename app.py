from flask import Flask, render_template, request

app = Flask(__name)

def calculate_gpa():
    num_subjects = int(request.form["num_subjects"])
    total_credits = 0
    total_grade_points = 0

    for i in range(num_subjects):
        subject_name = request.form[f"subject_name_{i}"]
        credit_hours = int(request.form[f"credit_hours_{i}"])
        grade = request.form[f"grade_{i}"]

        # Your grade to grade_points mapping code here

        total_credits += credit_hours
        total_grade_points += grade_points * credit_hours

    if total_credits == 0:
        gpa = 0.0
    else:
        gpa = total_grade_points / total_credits

    return f"Your GPA for this semester is: {gpa:.2f}"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        gpa = calculate_gpa()
        return render_template("result.html", gpa=gpa)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
