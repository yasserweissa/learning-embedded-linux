
searched_number = 2
count = 0
lst = [1, 2, 3, 4, 1, 2, 1, 1,1,1,1,1,1,1,1,1,1]

for item in lst:
    if item == searched_number:
        count += 1
print(f"The number {searched_number} was found {count} times in the list.")
