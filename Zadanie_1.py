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

numbers.remove(min(numbers))
numbers.remove(max(numbers))

print(numbers)

mean_number = sum(numbers) / len(numbers)

print(mean_number)
