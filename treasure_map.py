# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]

position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆
#as the input is in string we will have to change it into int
horizontal= int(position[  1])
vertical= int(position[0])

#Write your code below this row 👇
map[horizontal - 1] [vertical - 1] ="x"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇print(f"{row1}\n{row2}\n{row3}")
print(f"{row1} \n {row2} \n {row3}")
