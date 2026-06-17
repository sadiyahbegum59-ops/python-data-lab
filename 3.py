# Program 1: Word frequency

sentence = "apple banana apple mango banana apple"
words = sentence.split()
frequency = {}

print("Program 1")
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print(frequency)


# Program 2: Merge dictionaries

dict1 = {"a": 10, "b": 20}
dict2 = {"b": 5, "c": 15}

print("Program 2")
merged = dict1.copy()

for key, value in dict2.items():
    if key in merged:
        merged[key] += value
    else:
        merged[key] = value

print(merged)


# Program 3: Sort dictionary by values descending

data = {"A": 50, "B": 20, "C": 80}

print("Program 3")
sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)
print(sorted_data)


# Program 4: Key with maximum value

data = {"A": 50, "B": 80, "C": 80}

print("Program 4")
max_value = max(data.values())

for key, value in data.items():
    if value == max_value:
        print(key)


# Program 5: Invert dictionary

data = {"A": 1, "B": 2, "C": 1}
inverted = {}

print("Program 5")
for key, value in data.items():
    if value not in inverted:
        inverted[value] = [key]
    else:
        inverted[value].append(key)

print(inverted)
