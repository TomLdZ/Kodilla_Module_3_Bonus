numbers = [5, 32, 56, 2, 2, 16, 7, 10, 23, 100]
mean_number = 0

for num in numbers:
    if num % 10 == 0:
        continue
    elif num % 10 >= 5:
        numbers.insert(numbers.index(num), num + (10 - num % 10))
        numbers.remove(num)
    else:
        numbers.insert(numbers.index(num), num - num % 10)
        numbers.remove(num)

print(numbers)

smaller_num = 0
higher_num = 0

for num in numbers:
    if num < smaller_num:
        smaller_num = num 
    elif num > higher_num:
        higher_num = num

numbers.remove(smaller_num)
numbers.remove(higher_num)

print(numbers)

mean_number = sum(numbers) / len(numbers)

print(mean_number)
