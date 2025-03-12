# Get the number of elements
n = int(input("Enter the number of elements: "))

# Collect elements from the user
arr = [input(f"Enter element {i+1}: ") for i in range(n)]

# Brute-force approach to find the most occurring item
max_count = 0
most_common_item = None

for i in arr:
    count = 0
    for j in arr:
        if i == j:
            count += 1
    if count > max_count:
        max_count = count
        most_common_item = i

# Print the result
print(f"The most occurring item is '{most_common_item}' with {max_count} occurrences.")
