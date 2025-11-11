
try:
    number = int(input("Enter a number to display its multiplication table: "))
except ValueError:
    print("Invalid input. Please enter an integer.")
    exit()

print(f"Multiplication Table for {number}:")
for i in range(1, 11):  
    product = number * i
    print(f"{number} x {i} = {product}")