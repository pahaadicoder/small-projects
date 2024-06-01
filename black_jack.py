print(''' _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
                       _/ |                
                      |__/                 
''')
import random
print("welcome to the blackjack")

suits = ["♠", "♥", "♦", "♣"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


card_values = {
    "♠": 0,
    "♥": 0,
    "♦": 0,
    "♣": 0,
    "A": 11,  # or 11, depending on the game rules
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10
}

deck = [(rank, suit) for suit in suits for rank in ranks]
user= random.sample(deck,2)
print(user)
 
deck = [(rank, suit) for suit in suits for rank in ranks]
computer= random.sample(deck,2)
print(computer)

user_total =sum(card_values[card[0]] for card in user)
print(user_total)

computer_total =sum(card_values[card[0]] for card in computer)
print(computer_total)

if user_total ==21:
   result1= print("blackjack")
    
if computer_total ==21:
    result2=print("blackjack")
    
if result1 == result2:
    print("its a draw")

elif result1 =="blackjack" and result2 != "blackjack":
    print("u won")

elif result1 !="blackjack" and result2 == "blackjack":
    print("u lose")
    
print(''' _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
                       _/ |                
                      |__/                 
''')
import random
print("welcome to the blackjack")

suits = ["♠", "♥", "♦", "♣"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


card_values = {
    "♠": 0,
    "♥": 0,
    "♦": 0,
    "♣": 0,
    "A": 11,  # or 11, depending on the game rules
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10
}

deck = [(rank, suit) for suit in suits for rank in ranks]
user= random.sample(deck,2)
print(user)
 
deck = [(rank, suit) for suit in suits for rank in ranks]
computer= random.sample(deck,2)
print(computer)

user_total =sum(card_values[card[0]] for card in user)
print(user_total)

computer_total =sum(card_values[card[0]] for card in computer)
print(computer_total)

result1 = None
result2 = None

if user_total == 21:
    result1 = None
    result1 = "blackjack"
    print("User has a blackjack!")

if computer_total == 21:
    result2 = None
    result2 = "blackjack"
    print("Computer has a blackjack!")

result1 = None
if result1 == result2:
    print("It's a draw")
elif result1 == "blackjack" and result2 != "blackjack":
    print("You win!")
elif result1 != "blackjack" and result2 == "blackjack":
    print("You lose!")
