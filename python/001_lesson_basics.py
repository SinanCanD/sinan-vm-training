"""Lesson 1"""

# Task 1: Variables & Types

age = 20                    #int
height = 1.87               #float
favorite_lesson = "Math"    #string
is_student = True           #boolean

print("Types: ")
print(type(age))
print(type(height))
print(type(favorite_lesson))
print(type(is_student))



# Task 2: String Methods

word = "Programming"
print(word.upper())                     #Uppercase
print(word.lower())                     #Lowercase
print("Length:", len(word))             #Lenght
print("Substring: (0-3):", word[0:3])   #Substring



# Task 3: String Operations

sentence = "I love Programming Python"
print(sentence.replace("Python", "Ruby"))   #replace
print("Find 'is': ", sentence.find("is"))   #find
print("Split: ", sentence.split())          #split
print("Join: ", "-".join(["a", "b", "c"]))  #join



# Task 4: f-string

name = "Sinan"
age = 20
print(f"My name is {name} and I am  {age} years old")
print(f"In 5 years I will be {age + 5}")



# Task 5: User Input

user_name = input("Enter your name: ")
print(f"Hello {user_name}, Welcome!")



# Task 6: More variable examples

x = 10          # int
y = 2.5         # float
z = "25"        # str
flag = False    # bool

print(int(y))       
print(float(x))  
print(str(x))     
print(bool(z))     
print(bool(""))    



# Task 7: More string slicing

word = "Programming"
print(word[0])       # P
print(word[-1])      # g
print(word[0:6])     # Progra
print(word[::2])     # Pormig (every 2nd letter)
print(word[::-1])    # reversed string



# Task 8: More string methods

text = "  Python is Fun  "
print(text.strip())           # remove spaces from start/end
print(text.startswith("Py"))  # True
print(text.endswith("Fun"))   # False, because spaces
print(text.lower())           # python is fun
print(text.title())           # Python Is Fun



# Task 9: More f-string examples

pi = 3.14159
name = "Sinan"
age = 20

print(f"{name} is {age} years old. Pi is about {pi:.2f}")  # 2 decimals
print(f"In 3 years {name} will be {age + 3}")              # inline math
print(f"Name in upper: {name.upper()}")                    # method inside
