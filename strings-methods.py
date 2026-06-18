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



#.find() method - returns the index of the first occurrence of a substring in a string. If the substring is not found, it returns -1.
"""
text1 = "The quick brown fox jumps over the lazy dog"
print(text1.find("fox"))
"""




#.rfind() method - returns the index of the last occurrence of a substring in a string. If the substring is not found, it returns -1.
"""
text1 = "The quick brown fox jumps over the lazy dog"
print(text1.rfind("brown"))
"""



#.index() method - returns the index of the first occurrence of a substring in a string. If the substring is not found, it raises a ValueError.
"""
text1 = "The quick brown fox jumps over the lazy dog"
print(text1.index("cat"))
"""



#.count() method - returns the number of occurrences of a substring in a string (case-sensitive).
"""
text1 = "Hello Python"
print(text1.lower().count("h"))
"""



#startswith() method - checks if a string starts with a specified prefix. It returns True if the string starts with the prefix, and False otherwise (case-sensitive).
"""
text1 = "Hello Python"
print(text1.startswith("He"))
"""



#endswith() method - checks if a string ends with a specified suffix. It returns True if the string ends with the suffix, and False otherwise (case-sensitive).
"""
text1 = "Hello Python"
print(text1.endswith("on"))
"""



#center() - returns a new string that is centered within a specified width. It pads the string with a specified character (default is space) on both sides to achieve the desired width.
"""
text1 = "Welcome"
print(text1.center(20,"$"))
"""



#ljust() - returns a new string that is left-justified within a specified width. It pads the string with a specified character (default is space) on the right side to achieve the desired width.
"""
text1 = "Welcome"
print(text1.ljust(20,"$"))
"""



#rjust() - returns a new string that is right-justified within a specified width. It pads the string with a specified character (default is space) on the left side to achieve the desired width.
"""
text1 = "Welcome"
print(text1.rjust(20,"$"))
"""



#zfill() - returns a new string that is zero-padded on the left side to achieve a specified width.
"""
text1 = "Welcome"
print(text1.zfill(1000))
"""



#.isalpha() method - checks if all characters in a string are alphabetic (letters). It returns True if all characters are alphabetic and there is at least one character, otherwise it returns False (space-sensitive).
"""
text1= "Hello World"
print(text1.isalpha())
"""



#.isnumeric() - checks if all characters in a string are numeric (digits). It returns True if all characters are numeric and there is at least one character, otherwise it returns False (space-sensitive).
"""
text1= "½"
print(text1.isnumeric())
"""



#.isdigit() - checks if all characters in a string are digits. It returns True if all characters are digits and there is at least one character, otherwise it returns False (space-sensitive).
"""
text1= "½"
print(text1.isdigit())
"""



#.isalnum() - checks if all characters in a string are alphanumeric (letters and digits). It returns True if all characters are alphanumeric and there is at least one character, otherwise it returns False (space-sensitive).
"""
text1= "HelloWorld1234"
print(text1.isalnum())
"""



#isspace() - checks if all characters in a string are whitespace characters (spaces, tabs, newlines, etc.). It returns True if all characters are whitespace and there is at least one character, otherwise it returns False.
"""
text1= "         "
print(text1.isspace())
"""



#.islower() - checks if all characters in a string are lowercase letters. It returns True if all characters are lowercase and there is at least one character, otherwise it returns False (space-sensitive).
"""
text1= "Hello World"
print(text1.islower())
"""


#.isupper() - checks if all characters in a string are uppercase letters. It returns True if all characters are uppercase and there is at least one character, otherwise it returns False (space-sensitive).
"""
text1= "Hello World"
print(text1.isupper())
"""


#.istitle() - checks if a string is in title case (the first character of each word is uppercase and the rest are lowercase). It returns True if the string is in title case and there is at least one character, otherwise it returns False.
"""
text1= "Hello World"
print(text1.istitle())
"""



#.partition() and .rpartition() - partition() and rpartition() are string methods used to split a string into exactly three parts based on a specific separator. Both methods always return a tuple containing three elements.
"""
url_path = "users/profile/settings/avatar.jpg"
# Code - .partition()
before, sep, after = url_path.partition("/")
print("Before:", before)
print("Sep   :", sep)
print("After :", after)

# Code - .rpartition()
before, sep, after = url_path.rpartition("/")
print("Before:", before)
print("Sep   :", sep)
print("After :", after)
"""



#encode() - returns a bytes object representing the string encoded in the specified encoding (default is 'utf-8').
"""
text1 = "hello world"
print(text1.encode("utf-8"))
"""