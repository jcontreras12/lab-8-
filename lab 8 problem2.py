# Jose Contreras
# 11/22/21
# Write a function that takes two inputs from a user and prints whether the sum is greater than 10, less than 10, or equal to 10.
'''
i = int(input("Enter a number: "))
x = int(input(" Enter a different number: "))
n = 10
if i + x > n:
    print("The numbers is greater than 10")
if i + x < n:
    print(" The number is less than 10")
if i + x == n:
    print("The Number is equal to 10")
'''
def comp_ten(x, y):
    if  x + y > 10:
        print("The numbers is greater than 10")
    elif: x + y < 10:
        print(" The number is less than 10")
    else:
        print("The Number is equal to 10")
#test the function
x = int(input(" Enter a different number: "))
y = int(input(" Enter a different number: "))
comp_ten(x, y)

    
    
