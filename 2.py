# Program 1: Sum of 5 numbers

numbers = [10, 20, 30, 40, 50]
print("Program 1")
print("Sum =", sum(numbers))


# Program 2: Largest and smallest number

numbers = [15, 3, 78, 22, 9]
print("Program 2")
print("Largest =", max(numbers))
print("Smallest =", min(numbers))


# Program 3: Count even and odd numbers

numbers = [1, 2, 3, 4, 5, 6]
even = 0
odd = 0

print("Program 3")
for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even =", even)
print("Odd =", odd)


# Program 4: Remove duplicates

numbers = [1, 2, 2, 3, 4, 4, 5]
print("Program 4")
unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print(unique)


# Program 5: Reverse list without reverse()

numbers = [10, 20, 30, 40, 50]
print("Program 5")
reversed_list = numbers[::-1]
print(reversed_list)
