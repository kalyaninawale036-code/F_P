# Input the two numbers from the user
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Invalid input. Please enter numerical values.")
else:
    sum_result = num1 + num2
    difference_result = num1 - num2
    product_result = num1 * num2

    if num2 != 0:
        quotient_result = num1 / num2
        print(f"Sum: {sum_result}")
        print(f"Difference: {difference_result}")
        print(f"Product: {product_result}")
        print(f"Quotient: {quotient_result}")
    else:
        print(f"Sum: {sum_result}")
        print(f"Difference: {difference_result}")
        print(f"Product: {product_result}")
        print("Cannot calculate quotient: Division by zero is not allowed.")