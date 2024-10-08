# Find the second largest element in the array.

# Approach One

def findSecondLargest(numbers):
    numbers.sort()  # Sort the list in non-decreasing order
    totalNumbers = len(numbers)  # Get the total number of elements
    currentIndex = totalNumbers - 2  # Start checking from the second last element
    secondLargest = numbers[currentIndex]
    
    # Traverse backwards to find the second largest distinct element
    while currentIndex >= 0:
        if numbers[currentIndex] < numbers[-1]:  # Find the first element less than the largest
            secondLargest = numbers[currentIndex]
            break
        currentIndex -= 1
    
    return secondLargest

# Example usage
numbers = [1, 4, 6, 3, 8, 9, 0, 3]
result = findSecondLargest(numbers)
print(result)  # Output: 8



# Appraoch Two

numbers = [1, 4, 6, 3, 8, 9, 0, 3]
totalNumbers = len(numbers)

# Step 1: Find the largest element
largestElement = numbers[0]
for i in range(totalNumbers):
    if numbers[i] > largestElement:
        largestElement = numbers[i]

print("Largest Element:", largestElement)

# Step 2: Find the second largest element
secondLargestElement = -1
for i in range(totalNumbers):
    if numbers[i] > secondLargestElement and numbers[i] < largestElement:
        secondLargestElement = numbers[i]

print("Second Largest Element:", secondLargestElement)



# Approach Third

numbers = [1, 4, 6, 3, 8, 9, 0, 3]
totalNumbers = len(numbers)

largestElement = numbers[0]
secondLargestElement = -1

for i in range(1, totalNumbers):
    if numbers[i] > largestElement:
        secondLargestElement = largestElement  # Update second largest before changing the largest
        largestElement = numbers[i]
    elif numbers[i] > secondLargestElement and numbers[i] != largestElement:
        secondLargestElement = numbers[i]  # Update second largest if needed

print("Largest Element:", largestElement)
print("Second Largest Element:", secondLargestElement)

