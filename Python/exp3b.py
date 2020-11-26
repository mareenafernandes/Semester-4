user_list = []
line = input("Enter a list: ")

while(line != ''):
    user_list.append(line)
    line = input()

print(user_list)

word = input("Enter next element , if present won't be added ")
if word not in user_list:
    user_list.append(word)

print("Final list is ", user_list)
