
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

# print(map) 


column_position = int(position[0]) - 1
row_position = int(position[1]) - 1
# row_position[column_position]
map[column_position][row_position] = "💰"


print(f"{row1}\n{row2}\n{row3}")