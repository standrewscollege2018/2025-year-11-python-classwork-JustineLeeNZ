
keep_asking = True

while keep_asking == True:
    try:
        age = int(input("Age? "))
        keep_asking = False
    except ValueError:
        print("Enter an integer")

print("Success")
