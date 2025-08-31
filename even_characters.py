og_string = input("Enter any string: ")
print("Printing only even index chars")
len_string = len(og_string)
for i in range(len_string): 
    if i % 2 == 0 : 
        print(og_string[i])


   
    