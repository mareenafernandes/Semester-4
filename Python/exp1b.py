list_1 = list(range(1,51))
print(list_1)
a=int(input("Enter 1st slicing index : "))
b=int(input("Enter 2nd slicing index : "))
print(list_1[a:b])
c=int(input("Enter a number: "))
count=0
for i in list_1:
    if(i==c):
        break
    elif(c%i==0):
        count+=1
        print(count)
