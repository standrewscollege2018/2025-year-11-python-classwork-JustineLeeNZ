''' examples of lists - Justine '''

# examples of declaring different lists with different data types

# all string values
semi_finalists = ["Crusaders","Chiefs","Lions","Hurricanes"]

# all number values
grades = [100, 45, 99, 110, 95]

# mixture of data types
daily_stats = [17.5, "cloudy", 34, False]

# accessing an item in a list using an index
# first item has index = 0
print(semi_finalists[0])

# accessing an item in a list using an index of -1
# gets last item in the list
print(semi_finalists[-1])


# store list value as variable and print
current_semi_finalist = semi_finalists[2]
print(f"Current semi finalist is: {current_semi_finalist}")

# change the value of a list item
semi_finalists[2] = "Blues"
print(semi_finalists)

# add to the end of a list
print(grades)
# add new grade of 10
grades.append(10)
print(grades)

# deleting from a list, using an index
# delete first item in list i.e. index = 0
del grades[0]
print(grades)



