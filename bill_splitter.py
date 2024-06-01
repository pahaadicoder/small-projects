# Split string method
names_string = input("Give me everybody's names, separated by a coma.\n ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random
bill= random.randrange(0,len(names)-1)
print(f"{names[bill]}is going to buy the meal today!")