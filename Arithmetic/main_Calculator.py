'''
Building a simple calculator using python 
'''

username = input('Enter your name : ')
ask = input('What calculation u want? +,-,*,/  : ')


def Addition():
    var1 = int(input('Enter a number : '))
    var2 = int(input('Enter a number : '))
    solution = var1 + var2
    print(solution)

# Addition()

def subtraction():
    var1 = int(input('Enter a number : '))
    var2 = int(input('Enter a number : '))
    solution = var1 - var2
    print(solution)

# subtraction()

def multiplication():
    var1 = int(input('Enter a number : '))
    var2 = int(input('Enter a number : '))
    solution = var1 * var2
    print(solution)

# multiplication()

def Divide():
    var1 = int(input('Enter a number : '))
    var2 = int(input('Enter a number : '))
    solution = var1 / var2
    print(solution)

# Divide()


# Fulfling user demand 

if(ask == '+'):
    Addition()

elif(ask == '-'):
    subtraction()

elif(ask == '*'):
    multiplication()

elif(ask == '/'):
    Divide()

else:
    print(f'Wrong, choice choosen by {username} :')

