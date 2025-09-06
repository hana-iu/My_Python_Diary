print("This program removes the first (N) characters of a string")
literal_string = input ("Enter a string: ")
num_removed_char = int(input("Enter the number of characters you want to remove from the beginning of the string: "))
len_string = len(literal_string) 
if num_removed_char<0: 
    print("Error: Negative number is invalid!")
elif num_removed_char == 0 : 
    print(f"The string remains unchanged: {literal_string}")
elif num_removed_char >= len(literal_string): 
    print("The result is an empty string. ")
else: 
    new_string = literal_string[num_removed_char:]
    print(f"The new string is: {new_string}")
