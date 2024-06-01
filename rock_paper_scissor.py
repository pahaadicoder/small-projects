user= input('what do you choose\n')
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇0
import random
random.randint(0,2)
computer= (f"computer choose{computer}")
if computer==0 and user==0:
  print('its a draw')
elif computer==0 and user==1:
  print("you lost")
elif computer==0 and user==2:
  print("you won")
if computer==1 and user==1:
  print('you lost')
elif computer==0 and user==2:
  print("its a draw")
elif computer==2 and user==3:
  print("you won")
if computer==1 and user==1:
  print('you won')
elif computer==2 and user==0:
  print("you lost")
elif computer==1 and user==0:
  print("its a draw")

