def ciic3015_letter_grade_input():
    score = float(input("Enter your CIIC 3015 score (float): "))
    letter = ciic3015_letter_grade_param(score)
    print (f"Your letter grade is {letter}")

def ciic3015_letter_grade_param(score):
    # score = float(input("Enter your CIIC 3015 score (float): "))
    if score >= 90:
        return "Z"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 65:
        return "D"
    else:
        return "F"

