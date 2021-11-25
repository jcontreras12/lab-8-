# Jose Contreras
# 11/22/21
# Write a function that takes two inputs from a user and prints whether the sum is greater than 10, less than 10, or equal to 10.
i = int(input("Enter a number: "))
x = int(input(" Enter a different number: "))
n = 10
if i + x > n:
    print("The numbers is greater than 10")
if i + x < n:
    print(" The number is less than 10")
if i + x == n:
    print("The Number is equal to 10")