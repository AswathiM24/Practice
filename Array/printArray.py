# Get the number of elements
n = int(input("Enter the number of elements: "))

# Initialize an empty array
arr = []

# Collect elements from the user
for i in range(n):
    element = input(f"Enter element {i+1}: ")
    arr.append(element)

# Print the elements of the array
print("Elements of the array:")
for element in arr:
    print(element)
