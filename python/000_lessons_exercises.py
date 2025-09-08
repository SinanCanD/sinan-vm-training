# Exercises

print("=============================================================================")
# Lesson 001 Exercise 1:
# Create variables for your name, age, height, and favorite subject.
# Print them all in one sentence using an f-string.

name = "Sinan"
age = 20
height = 1.87
favorite_lesson = "Math"
print(f"My Name is {name}, I am {age} years old, {height} meters tall and my favorite subject is {favorite_lesson}")


print("=============================================================================")
# Lesson 001 Exercise 2:
# Take a string and:
# 1. Print the length of the string
# 2. Print the first 3 letters
# 3. Print the last 2 letters
# 4. Print the string reversed

word = "Python"
print(word)
print("1.Length: ", len(word))
print("2.First 3 letters: ", word[0:3])
print("3.Last 3 letters: ", word[-3:])
print("4.Reversed: ", word[::-1])


print("=============================================================================")
# Lesson 001 Exercise 3:
# Work with the string: "I love Python programming"
# 1. Replace "Python" with "Java"
# 2. Find the position of "love"
# 3. Split the sentence into words (list)
# 4. Join the list back into a string with "-" between the words

sentence = "I love Python programming"
print(sentence)
print("1.Replace Python with Java: ", sentence.replace("Python", "Java"))
print("2. Find the position of love: ", sentence.find("love"))
print("3. Split the sentence into words (list): ", sentence.split())
print("4. Join the list back into a string with '-' between the words", "-".join(sentence.split()))


print("=============================================================================")
# Lesson 001 Exercise 4:
# Use variables and f-strings
# 1. Create variables: product = "Laptop", price = 999.99, quantity = 3
# 2. Print one line: "I bought 3 Laptops for a total of 2999.97 EUR"
#    (Hint: use f-string and calculate total inside it)
# 3. Print price with only 2 decimals (999.99)

product = "Laptop"
price = 999.99
quantity = 3
print(f"I bought {quantity} {product}s for a total of {price * quantity:.2f} EUR")


print("=============================================================================")
# Lesson 001 Exercise 5:
# Work with strings and f-strings
# 1. Create a variable text = "   Python Basics   "
# 2. Remove the spaces on both sides
# 3. Print the text in uppercase
# 4. Print the length of the cleaned text
# 5. Use an f-string to print: "The word 'Python Basics' has X letters"
#    (replace X with the correct number)

text = "   Python Basics   " # 1. Create a variable text = "   Python Basics   "
print("2.Remove the spaces on both sides: ", text.strip())
print("3.Print the text in uppercase: ", text.upper())
print("4.Print the length of the cleaned text: ", len(text.strip()))
print(f"5. The word 'Python Basics' has {len(text.strip())} letters")


print("=============================================================================")
# Lesson 001 Exercise 6:
# Use the string: "Programming in Python"
# 1. Check if the string starts with "Pro"
# 2. Check if the string ends with "Java"
# 3. Convert the string to lowercase
# 4. Replace "Python" with "JavaScript"
# 5. Use an f-string to print:
#    "Does the text start correctly? True/False"
#    "Does the text end correctly? True/False"

sentence = "Programming in Python"
result_start = sentence.startswith("Prog")
result_end = sentence.endswith("Java")
print("1.Check if the string starts with 'Pro': ", sentence.startswith("Pro"))
print("2.Check if the string ends with 'Java': ", sentence.endswith("Java"))
print("3.Convert the string zo lowercase: ", sentence.lower())
print("4.Replace 'Python' with 'JavaScript': ", sentence.replace("Python", "JavaScript"))
print(f"5.Does the text start correctly? {result_start}")
print(f"5.Does the text end correctly? {result_end}")


print("=============================================================================")
# Lesson 001 Exercise 7:
# Work with variables and f-strings
# 1. Create variables: first_name = "Sinan", middle_name = "Can"
# 2. Print "My name is Sinan Can"
# 3. Print "My name in uppercase is SINAN CAN"
# 4. Print "The initials are S.C."

first_name = "Sinan"
middle_name = "Can"
print(f"2.Print 'My name is Sinan Can': My name is {first_name} {middle_name}")
print(f"3. Print 'My name in uppercase is SINAN CAN': My name in uppercase is {first_name.upper()} {middle_name.upper()}")
print(f"4. Print 'The initials are S.C.': The initials are {first_name[0]}.{middle_name[0]}.")


print("=============================================================================")
# Lesson 001 Exercise 8:
# Work with numbers and f-strings
# 1. Create variables: a = 7, b = 3
# 2. Print the sum (+) 
# 3. Print the difference (-)
# 4. Print the product (*)
# 5. Print the result of division (/) with 2 decimals
# 6. Use f-strings so the output looks like:
#    "7 + 3 = 10"
#    "7 - 3 = 4"
#    ...

a = 7
b = 3
print(f"a = {a}, b = {b}")
print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b:.2f}")


print("=============================================================================")
# Lesson 001 Exercise 9:
# Combine variables and strings with f-strings
# 1. Create variables: city = "Munich", country = "Germany", population = 1_500_000
# 2. Print: "Munich is a city in Germany."
# 3. Print: "It has about 1500000 people."
# 4. Print: "Population with commas: 1,500,000"
#    (Hint: use f-string with format specifier)

city = "Munich"
country = "Germany"
population = 1_500_000
print(f"{city} is a city in {country}")
print(f"It has about {population} people")
print(f"Population with commas: {population:,}")


print("=============================================================================")
# Lesson 001 Exercise 10:
# Practice everything from Lesson 001
# 1. Create variables: title = "Python", version = 3, year = 2025
# 2. Print: "Python version 3 was released in 2025"
# 3. Make the title uppercase
# 4. Print the length of the title
# 5. Combine all into one f-string:
#    "PYTHON (6 letters) - version 3 (year 2025)"

title = "Python" 
version = 3
year = 2025
print(f"{title} version {version} was released in {year}")
print(f"{title.upper()} version {version} was released in {year}")
print(f"{title.upper()} ({len(title)} letters) - version {version} (year {year})")