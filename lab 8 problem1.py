# Jose Contreras
# 11/22/21
# Write a function that takes two inputs from a user and prints whether they are equal or not
i = int(input("Enter a number: "))
x = int(input(" Enter a different number: "))
if i == x:
    print("The numbers are equal")
else:
    print("Number are not equal")
'''
1 define a function
2. get two inputs
3. call the function with passing the two inputs.
'''
def equal_number(x,y):
    if num1 == num2:
        print("The two numbers are equal to each other")
    else:
        print("The numbers are not equal. Try again.")
    
    
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
equal_number(num1, num2)
