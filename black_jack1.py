import random

def deal_card():
    cards= [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card= random.choice(cards)
    return card

def calculate_score(cards):
    '''take a list of cards and return the score calculated from the cards '''
    return sum(cards)
    
#if 11 in cards and 10 in cards and len(cards) ==2:
    if sum(cards) ==21 and len(cards) ==2:
        return 0   #hence indicating black jack instead of returnng the total
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score,computer_score):
    if user_score == computer_score:
        return "Draw \n"
    elif computer_score == 0:
        return "Lose , opponent has blackjack \n"
    elif user_score == 0:
        return "win with a blackjack \n"
    elif user_score >21:
        return "you went over 21  \n . you lose"
    elif computer_score>21:
        return "opponent went over 21 \n. you win "
    elif user_score>computer_score:
        return "you win \n"
    else:
        return "you lose \n"
    
    
    
user_cards= []
computer_cards=[]
is_game_over = False

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"yours card: {user_cards},cureent score:{user_score}")

    print(f"computer's first card: {computer_cards[0]}")


    if user_score ==0 or computer_score ==0 or user_score >21:
        is_game_over= True
    else:
        user_should_deal=input("type 'y' to get another card or 'n' for no ")
        if user_should_deal == 'y':
            user_cards.append(deal_card())
        else:
            is_game_over = True


while computer_score !=0 and computer_score <17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
    
    
print(compare(user_score,computer_score))






    