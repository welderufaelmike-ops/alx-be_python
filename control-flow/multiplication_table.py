
number = int(input("Enter a number to see its multiplication table:"))
print(number)
for y in range(1, 11):
    z = number*y

    print (f"{number} * {y} =  {z}" )