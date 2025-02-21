''' examples of while loops - Justine Lee '''

# example of while loop syntax but should really use for loop
'''
number = 0

while number < 10:
    print(number)
    number = number + 1

print("All done")
'''
# using a Boolean

# set Boolean to True to control loop
keep_asking = True

#start asking for a name
while keep_asking == True:
    name = input("Enter your name: ")

    if name == "Ethan":
        keep_asking = False
    else:
        print("Wrong name")

#loop exited so do something else e.g. greet Ethan
print("Hi Ethan")

