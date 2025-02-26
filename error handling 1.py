# error handling examples

# boundary conditions

# variable to control while loop
keep_asking = True

# keep looping until valid age entered
while keep_asking == True:
    # ask for age, must be > 0
    age = int(input("Age? "))

    # check for boundary
    if age > 0 and age<=100:
        keep_asking = False
    else:
        print("Enter an age > 0")


# have valid age, check if can site licence
if age > 16:
        print("You can sit your Learners licence")
else:
    print("sorry you have to wait")
