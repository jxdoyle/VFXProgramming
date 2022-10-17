import os
os.system('cls' if os.name == 'nt' else 'clear')

# def <name>(arg1, arg2, ..., argN):​
#   <statements> return <value>​

def multiply(x, y, a = 10, b = 20):
    """
    Multiply the arguments and return result \n
    Code Document String: multi-line \n
    Used to explain how to use function to programmers \n
    We can return multiple values from a function \n
    Keyword  arguments: \n
    x -- x value (default = 0) \n
    y -- y value (default = 0) \n
    a -- a value (default = 10) \n
    b -- b value (default = 20) \n

    Keyword return: \n
    result = x * y * a * b \n
    """
    result = x * y * a * b
    return result

