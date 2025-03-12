# Get the number of elements
n = int(input("Enter the number of elements: "))

# Collect elements from the user
arr = [input(f"Enter element {i+1}: ") for i in range(n)]

# Print the array in reverse order using slicing
print("Array in reverse order:", arr[::-1])
