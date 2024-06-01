import random
print("welcome to the hangman")
print("guess the world")
animals=["cow","buffalow","giraffe","sheep","dog","lion","tiger","horse","rabbit"]
pc=random.choice(animals)
free_pc=list(pc)
user=input("answer\n").lower()
for letter in free_pc:
    if letter==user:
        print("success")
    else:
        print("failure")
                      
