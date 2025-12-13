"""
 Challenge: Student Marks Analyzer

Create a Python program that allows a user to input student names along with their marks and then calculates useful statistics.

Your program should:
1. Let the user input multiple students with their marks (name + integer score).
2. After input is complete, display:
   - Average marks
   - Highest marks and student(s) who scored it
   - Lowest marks and student(s) who scored it
   - Total number of students

Bonus:
- Allow the user to enter all data first, then view the report
- Format output clearly in a report-style layout
- Prevent duplicate student names
"""


def collect_student_data():
    students = {}
    
    while True:
        name = input("Enter the student name or enter done to exit: ").strip()
        if name.lower()== "done":
            break
        if name in students:
            print("Student Already exists")
            continue

        try:
            marks= float(input(f"Enter Marks for {name}: "))
            students[name] =marks
        except ValueError:
            print("Please enter a valid number for marks")
        print("If All students data filled please Type 'done' to exit")
    return students

def display_report(students):
    if not students:
        print("No Student Data ❌")
        return
    
    marks= list(students.values())
    max_score=max(marks)
    min_score= min(marks)
    average= sum(marks)/len(marks)
    total_student= len(students)
    
    topper = [name for name, score in students.items() if score== max_score ]
    lower = [name for name, score in students.items() if score== min_score ]

    print("\n Students marks report 📑 \n")
    print("_" * 31)
    print(f"-Average marks: {average:.2f}")
    print(f"-Highest marks: {max_score} by {', '.join(topper)}")
    print(f"-lowest marks: {min_score} by {', '.join(lower)}\n")
    print(f"-Total Number of student: {total_student}")


    print("_" * 31)
    print("Detailed marks📊")

    for name, score in students.items():
        print(f" - {name}: {score}")

def main():
    students=collect_student_data()
    display_report(students)


if __name__ == "__main__":
    main()