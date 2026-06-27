#sample - function definition
"""
def main():
    name = input("enter your name:")
    Hello(name)

def Hello(random="name"):
    print("Hello",random)

main()
"""

#calculator - function definition

def calculator():
    def addition(a,b):
        print("Addition of two values is:", a+b)
        return addition
    
    def subtraction(a,b):
        print("Subtraction of two values is:",abs(a-b))

    def multiply(a,b):
        print("Multiplication of two values is:", a*b)

    def division(a,b):
        if b!=0:
            print("Division of two values is:", round(a/b))
        else:
            print("Division by zero is not allowed")

"""
def calculator(a,b):
    print("Addition of two values is:", a+b)
    print("Subtraction of two values is:",abs(a-b))
    print("Multiplication of two values is:", a*b)
    if b!=0:
        print("Division of two values is:", round(a/b))
    else:
        print("Division by zero is not allowed")
"""


def main():
    n1 = float(int(input("Enter First Number:")))
    n2 = float(int(input("Enter Second Number:")))
    add = calculator.addition(n1,n2)
    print (add)
    
main()