#This is sample program to demonstrate the String Concatenation - type error - Python cannot combine a string and an integer directly.
"""name = input ("Enter your name:")
age = int (input ("Enter age:"))
print ("Hello I am "+ name + ", " + age + " years.")
print("My name is " + name + " and I am " + age)
"""
#string concatenation "+" becomes messy when multiple variables are involved. The ".format()" method is a better way to combine string and integer values.


#Sample program to demonstrate the usage of ".format()" method to combine string and integer values.
"""
name = input ("Enter ur name: ")
age = int(input("Enter ur age: "))
print ("My name is {}, {} years ".format(name,age))
print("My name is {1} and I am {0}".format(name, age))
print("My name is {n} and I am {a}".format(n=name, a=age))
"""
#.format() Although cleaner than concatenation, it still feels repetitive. - simpler syntax is f-strings.



#Demonstration of f-strings (A.K.A Formatted String Literals) - introduced in Python 3.6 - allows you to embed expressions inside string literals, using curly braces {}.
"""
name = input ("Enter ur name: ")
age = int(input("Enter ur age: "))
print(f"My name is {name}, {age} years old.")
"""