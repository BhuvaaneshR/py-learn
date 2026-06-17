#.capitalize() method - Converts first character to uppercase and remaining characters to lowercase.
"""
text1 = "hELLO WORLD"
text1 = text1.capitalize()
print (text1)
"""



#.title() method - Capitalizes first letter of every word.
"""
text1 = "hELLO WORLD"
text1 = text1.title()
print (text1)
"""



#.strip() method - removes whitespace across starting and ending of a string.
"""
text1 = "hELLO WORLD                   "
text1 = text1.strip()
print (text1)
"""



#.upper() method - converts all characters to uppercase.
"""
text1 = "HelloWorld"
text1 = text1.upper()
print (text1)
"""



#.lower() method - converts all characters to lowercase.
"""
text1 = "HelloWorld"
text1 = text1.lower()
print (text1)
"""



#.casefold() method - converts all characters to lowercase and is more aggressive than lower() method. It is used for caseless matching.
"""
text1 = "HelloWorld"
text1 = text1.casefold()
print (text1)
"""



#.swapcase() method - converts uppercase characters to lowercase and lowercase characters to uppercase.
"""
text1 = "HelloWorld"
text1 = text1.swapcase()
print (text1)
"""



#.lstrip() method - removes whitespace from the left side of a string.
"""
text1 = "     Hello World"
text1 = text1.lstrip()
print (text1)
"""



#.rstrip() method - removes whitespace from the right side of a string.
"""
text1 = "Hello World     "
text1 = text1.lstrip()
print (text1)
"""



#.splitlines() method - splits a string into a list of lines. It splits at line breaks and returns a list of lines in the string.
"""
text1 = "Hello\n World\r Python"
text1 = text1.splitlines()
print (text1)
"""



#.join() method - joins the elements of an iterable (e.g., list, tuple) into a single string, using a specified separator.
"""
word = ["hello", "hi", "hello"]
print(f" ".join(word))
"""