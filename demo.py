 
 
import random

print("welcome to the higher or lower game")


score = 0

def randomizer():
    global play_again,score
    while play_again: 
        celebrity_list = ['rihana', 'katrina' , 'kohli' , 'dhoni', 'jadeja', 'varun_dhawan', 'ronaldo', 'messi' , 'taylor_swift', 'alia_bhatt' , 'Chris_gale', 'Irfan_Khan']
        celebrity1_list = ['justin_beeber', 'Mr_Beast' , 'ARpit' , 'Shivam' , 'Rishi', 'Nishant' , 'Begu', 'Yashvanta', 'anjali', 'Pallavit', 'Dheetan' , 'Sushant']
        followers_list = ['1000' , '1500', '2000', '2500','3000', '3500', '4000' , '4500', '5000', '5500', '60000']


        celebrity_1= random.choice(celebrity_list)

        celebrity_2 = random.choice(celebrity1_list)

        print(f"who has higher followers b/w  \t {celebrity_1}\t and \t {celebrity_2} \n \n")
        
        user = input("please enter A for celebrity_1 and B for celebrity_2 \n \n").upper()
        
        if user not in ['A', 'B']:
            print("Invalid input. Please enter 'A' or 'B'.")
            return False  # Return False to indicate no restart


        followers1 = random. choice(followers_list)

# Remove the first number from the list to avoid duplicates
        followers_list.remove(followers1)


        followers2 = random. choice(followers_list)

        
        if (followers1 > followers2 and user=='A' ) or (followers1 < followers2 and user=='B' ):
            result=print("you win")
            score +=1
            play_again = True

        else:
            print("You lose!")
            play_again = False
            
        print(f"Your current score: {score}\n")


play_again = True
while play_again:
    play_again = randomizer()
    




    
 