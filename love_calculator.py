# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combined= name1+name2
lower_string=combined.lower()
t=lower_string.count("t")
r=lower_string.count("r")
u=lower_string.count("u")
e=lower_string.count("e")
l=lower_string.count("l")
o=lower_string.count("o")
v=lower_string.count("v")
e=lower_string.count("e")
total_true= str(t+r+u+e)
total_love=str(l+o+v+e)
score=int(total_true+total_love)
print(f"your love score is {score}")
if (score<10) or (score>90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score>40) or (score<50):
  print(f"Your score is {score},you are alright together.")
else:
  print(f"Your score is {score}.")