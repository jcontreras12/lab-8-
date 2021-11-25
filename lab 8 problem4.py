# Jose Contreras
# 11/22/21
#  Write a function that takes a year as a parameter and returns True if the year is a leap year, False if it is otherwise
def isleap(year):
    leap = False
    if (year % 4== 0) and (year % 100 != 0):
        leap = True
    elif (year % 100 == 0) and (year % 100 != 0):
        leap = False
    elif (year % 400 == 0):
        leap = "Yes, it is a leap year"
    else:
        leap = "No, it is not a leap year"
    return leap
year = int(input(" Enter a Year: "))
print(isleap(year))