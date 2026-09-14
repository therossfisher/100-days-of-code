student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

# builds a new empty dictionary
student_grades ={}


# use .items() to get both key and value together for each entry
# in this case name = the student score = that students number
for name, score in student_scores.items():
    if score >= 91:
        student_grades[name] = "Outstanding"
    elif score >= 81 and score < 90:
        student_grades[name] = "Exceeds Expectations"
    elif score >= 71 and score < 80:
        student_grades[name] = "Acceptable"
    elif score < 70:
        student_grades[name] = "Fail"


for key in student_grades:
    print(key)
    print(student_grades[key])