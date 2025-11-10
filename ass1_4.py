try:
    marks = float(input("Enter the marks: "))

    if marks >= 90:
        grade = 'A'
    elif marks >= 80: 
        grade = 'B'
    elif marks >= 70:
        grade = 'C'
    elif marks >= 60:
        grade = 'D'
    else:
        grade = 'F'

    print(f"The grade is: {grade}")

except ValueError:
    print("Invalid input. Please enter a numeric value for marks.")