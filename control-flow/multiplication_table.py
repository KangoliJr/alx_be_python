try:
    number = int(input("Enter a number to see its multiplication table:"))
except ValueError:
    print("Invalid input. Please enter a whole number")
    exit()
    
# generating multiplication table
print(f"Multiplication table for {number}:")
for i in range(1, 11):
    product = number * i
    print(f"{number} * {i} = {product}")