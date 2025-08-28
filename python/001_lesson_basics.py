"""Lesson 1"""

number = 21
pi = 3.14159
name = "Sinan"
student = True
nothing = None

print("Types:", type(number), type(pi), type(name), type(student), type(nothing))
print(number, pi, name, student, nothing)

#########################

as_text = str(number)
as_int = int("17") 
print("Casting:", as_text, as_text)

greeting = "Hello"
print(greeting.capitalize())
print(greeting.upper())
print("Length: ", len(greeting))
print("Substring: ", greeting[1:4])