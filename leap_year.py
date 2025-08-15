year = int(input("Enter year to be checked: "))
if (year%4 == 0  and year%100 != 0 or year%400 ==0):
    print("The year is a leap year")
else: 
    print("The year isn't a leap year!")
#A leap year, is a year that its number is divisible by 4 and not divisible by 100 and divisible with 400
"""What happens if you enter a value as 2000, first 2000%4 == 0 is true but 2000% 100 != 0 is not true, 2000%400 == 0 is true. 
 so, true and false or true, (and) is done first and then the (OR) so t&f = f  , f|t = t. So, yes 2000 is a leap year """