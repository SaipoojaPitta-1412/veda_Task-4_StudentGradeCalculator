def get_valid_mark(subject_name):
    """Prompts the user for a mark and validates that it is between 0 and 100."""
    while True:
        try:
            mark = float(input(f"Enter marks for {subject_name} (0-100): "))
            if 0 <= mark <= 100:
                return mark
            print("  [!] Error: Marks must be between 0 and 100. Try again.")
        except ValueError:
            print("  [!] Error: Please enter a numeric value. Try again.")


def calculate_grade(percentage):
    """Returns the letter grade based on the total percentage."""
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F (Fail)"


def main():
    print("========================================")
    print("       STUDENT GRADE CALCULATOR         ")
    print("========================================\n")

    # 1. Input Section
    subjects = ["Math", "Science", "English"]
    marks = {}

    for subject in subjects:
        marks[subject] = get_valid_mark(subject)

    # 2. Calculation Section
    total_marks = sum(marks.values())
    max_marks = len(subjects) * 100
    percentage = (total_marks / max_marks) * 100
    grade = calculate_grade(percentage)

    # 3. Output Section
    print("\n========================================")
    print("            SUMMARY REPORT              ")
    print("========================================")
    for subject, score in marks.items():
        print(f" {subject:<10} : {score:>6.2f} / 100")

    print("----------------------------------------")
    print(f" Total Marks : {total_marks:>6.2f} / {max_marks}")
    print(f" Percentage  : {percentage:>6.2f}%")
    print(f" Grade       : {grade:>6}")
    print("========================================")


if __name__ == "__main__":
    main()