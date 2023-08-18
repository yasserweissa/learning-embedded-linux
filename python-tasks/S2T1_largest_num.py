def find_largest_number(numbers):
    if not numbers:
        return None
    
    largest = numbers[0]
    
    for num in numbers:
        if num > largest:
            largest = num
            
    return largest

number_list = [34, 12, 78, 45, 90, 56]
largest_number = find_largest_number(number_list)

if largest_number is not None:
    print(f"The largest number is: {largest_number}")
else:
    print("The list is empty.")

