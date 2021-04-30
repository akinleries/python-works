def add(num1:int, num2:int)->int:
    return num1 + num2


def subtract(num1:int, num2:int)->int:
    return num1 - num2


def multiply(num1:int, num2:int)->int:
    if type(num1) != int or  type(num2) != int:
        if type(num1) != float or type(num2) != float:
            raise TypeError(TypeError, print("abeg input beta number"))
    return num1 * num2


def divide(num1:int, num2:int)->float:
    return num1 / num2
