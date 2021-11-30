# Jose Contreras
# 11/22/21
# Write a function that takes a list and prints if the value 5 is in that list.
'''
If 5 is found in the passed list, the list is printed. 
'''


#List = (1, 2, 3, 4, 5)
#for number in List:
#    if number < 5:
#        print(number)

List = [1, 2, 3, 4, 5]

def find_five(Lst):
    value = 5
    if value not in Lst:
        print(Lst)
    else:
        print("{} is not founc.".format(value))
        
#test the function
find_five(List)
