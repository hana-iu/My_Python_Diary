ch = input("Enter any character: ")
if(ch>='a' and ch<='z') or (ch>='A' and ch<='Z'):
    print(f"{ch} is an alphabet.")
else: 
    print(f"{ch} is not an alphabet")
"""python compares characters using their Unicode/ASCII values behind the scenes. as 
when you write if (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z'):
Python checks if ch falls within the Unicode range (a-z) or (A-Z).
 This is a direct comparison, not iteration of alphabet letters"""