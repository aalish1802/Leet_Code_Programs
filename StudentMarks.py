a = input("Students Name")
b = int(input("Enter Marks"))

if b >= 50:
    print("Pass")
else:
    print("Fail")

if b >= 90:
    print("A")
elif b >= 70 and b < 90:
    print("B")
elif b >= 50 and b < 70:
    print("C")
else:
    print("F")
