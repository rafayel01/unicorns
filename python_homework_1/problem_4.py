x = int(input("Enter a number from 1 to 8 for X coordinate: "))
y = int(input("Enter a number from 1 to 8 for Y coordinate: "))

if (x + y) % 2 == 0:
    print("Black")
else:
    print("White")

