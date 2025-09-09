"""Lesson 2 – Control Flow"""



print("=" * 75)
# Task 1: if/else (even or odd)
n = 7
print(n)
if n % 2 == 0:
    print("even")
else:
    print("odd")



print("=" * 75)
# Task 2: if/elif/else (simple grading)
score = 68
if score >= 80:
    print("grade: A")
elif score >= 60:
    print("grade: B")
else:
    print("grade: C")



print("=" * 75)
# Task 3: while (count 1..5)
i = 1
while i <= 5:
    print(i)
    i += 1



print("=" * 75)
# Task 4: for (iterate a list)
animals = ["cat", "dog", "fox"]
for a in animals:
    print(a)



print("=" * 75)
#Task 5: range (numbers)
for x in range(1, 6):      # 1,2,3,4,5
    print(x)
print("evens 0..10:")
for x in range(0, 11, 2):  # 0,2,4,6,8,10
    print(x)



print("=" * 75)
# Task 6: enumerate (index + value)
fruits = ["apple", "banana", "cherry"]
for idx, f in enumerate(fruits, start=1):
    print(idx, f)



print("=" * 75)
# Task 7: list comprehensions (very basic)
nums = [1, 2, 3, 4, 5]
squares = [x * x for x in nums]
evens = [x for x in nums if x % 2 == 0]
print("squares:", squares)
print("evens:", evens)



print("=" * 75)
# Task 4 – more: iterate strings and build a new list
for ch in "Python":
    print("char:", ch)
    
upper_animals = []
for a in animals:                 # animals = ["cat", "dog", "fox"]
    upper_animals.append(a.upper())
print("upper_animals:", upper_animals)   # ['CAT', 'DOG', 'FOX']



print("=" * 75)
# Task 5 – more: ranges and simple sums"
print("range(5):", list(range(5)))           # [0,1,2,3,4]
print("range(2,7):", list(range(2, 7)))      # [2,3,4,5,6]
print("range(10,0,-2):", list(range(10, 0, -2)))  # [10,8,6,4,2]

total = 0
for x in range(1, 11):  # 1..10
    total += x
print("sum 1..10:", total)  # 55

print("countdown 5..1:")
for x in range(5, 0, -1):
    print(x)



print("=" * 75)
# Task 6 – more: enumerate with different starts
for idx, f in enumerate(fruits):  # fruits = ["apple","banana","cherry"]
    print(f"index {idx}: {f}")    # startet bei 0

for idx, f in enumerate(fruits, start=1):
    print(f"{idx}) {f}")          # startet bei 1 (oft schöner)

for idx, f in enumerate(fruits, start=100):
    print(f"{idx}: {f}")          # Start beliebig wählbar



print("=" * 75)
# Task 7 – more: list comprehensions (simple)
nums = list(range(1, 11))
odd_nums = [x for x in nums if x % 2 == 1]
triple_nums = [x * 3 for x in nums]
print("odd numbers:", odd_nums)
print("triples:", triple_nums)

# Länge der Wörter
fruit_lengths = [len(f) for f in fruits]                 # [5, 6, 6]
print("fruit lengths:", fruit_lengths)

# Nur lange Wörter in UPPERCASE (>= 6 Zeichen)
upper_long_fruits = [f.upper() for f in fruits if len(f) >= 6]
print("upper_long_fruits:", upper_long_fruits)           # ['BANANA', 'CHERRY']

# Whitespace säubern mit Comprehension
names_raw = ["  Sinan ", " Ada", " Max  "]
names_clean = [n.strip() for n in names_raw]
print("names_clean:", names_clean)                       # ['Sinan', 'Ada', 'Max']
