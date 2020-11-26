user_str = input("Enter string to remove punctuations: ")

import string
for c in string.punctuation:
    user_str = user_str.replace(c,"")

print(user_str)
