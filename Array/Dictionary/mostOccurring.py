# Get the number of elements
n = int(input("Enter the number of elements: "))

# Collect elements from the user
arr = [input(f"Enter element {i+1}: ") for i in range(n)]

# Dictionary to store frequency count
freq = {}

# Count occurrences of each element
for item in arr:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1

# Find the most occurring element
most_common_item = max(freq, key=freq.get)
max_count = freq[most_common_item]

# Print the result
print(f"The most occurring item is '{most_common_item}' with {max_count} occurrences.")
