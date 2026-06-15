'''
In this, program I've write the code to solve any custom equation Which is writtend in this form  :
a quadratic polynomial (y = ax² + bx + c) 

'''
name = input("Enter your name : ")

sum1 = input('Enter a variable eg: (x,y,z) : ')
sum2 = input('Enter a exponnet power for variable eg:(2,3,4,5) : ')
sum3 = input('Enter a Digit eg:(1,2,3) : ')
sum4 = input('Enter a variable eg:(x,y,z) : ')
sum5 = input('Enter a Digit eg:(1,2,3) : ')
sum6 = input('Enter a Digit eg:(1,2,3)')

finaleq =  (f"{sum3}{sum1}^{sum2} + {sum5}{sum4} + {sum6}")
print(f'Dear {name} your equation is {finaleq}')
