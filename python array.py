numbers = [10, 25, 7, 99, 45]

largest = numbers[0]   # Start with the first element

for num in numbers:
    if num > largest:
        largest = num

print("Largest number is:", largest)
