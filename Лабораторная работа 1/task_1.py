numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

index_none_number = 4
numbers[index_none_number] = 0

count_of_numbers = len(numbers)
sum_of_numbers = sum(numbers)

numbers[index_none_number] = sum_of_numbers / count_of_numbers
print("Измененный список:", numbers)
