
size=int(input("enter the size of the pattern:"))
while size<=0:
    print("enter postive number")
    size=int(input("enter the size of the pattern: "))
row=0
while row < size:
    for col in range(size):
        print("*" , end= "")
    print()
    row+=1