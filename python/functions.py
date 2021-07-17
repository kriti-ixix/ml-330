'''
Types of functions:
Parameters:
- Default Method
- Parameterised Method

Return type:
- No return type
- Return type
'''

def addNumbers():
    x = 10
    y = 20
    print("The sum is {}".format(x+y))

def subNumbers(a, b):
    print("The difference is", a-b)

def multiplyNumbers(a, b, c):
    product = a * b * c
    return product


addNumbers()
subNumbers(50, 40)
p1 = multiplyNumbers(10, 20, 30)