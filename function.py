def count_numbers(numbers):
    counts = {}
    for num in numbers:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    return counts

my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4,9]
result = count_numbers(my_list)
print(result)
