try:
    size = int(input("Enter the size of the pattern:"))
    if size <= 0:
        print("Enter a positive integer")
        exit()
except ValueError:
    print("Invalid input. Please enter a whole number.")
    exit()
    
# drawing the pattern
row_count = 0
while row_count < size:
    for _ in range(size):
        print("*", end="")
    print()
    row_count += 1