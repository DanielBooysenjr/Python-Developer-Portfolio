# π¨ Don't change the code below π
row1 = ["π","οΈπ","οΈπ"]
row2 = ["π","π₯°","οΈπ"]
row3 = ["π½οΈ","πΎοΈ","π€οΈ"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# π¨ Don't change the code above π

#Write your code below this row π

horizontal = int(position[0])
verticle = int(position[1])

selected_row = map[verticle -1]
selected_row[horizontal -1] = "X"

#Write your code above this row π

# π¨ Don't change the code below π
print(f"{row1}\n{row2}\n{row3}")

