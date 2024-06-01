message= input("please enter your message \n")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
shift= int(input("type the shift number \n"))
direction = input("type encode or decode \n")


def decrypt(message,shift):
    decipher_text = ""
    for letter in message:
        position = alphabet.index(letter)
        new_position = position - shift
        new_letter= alphabet[new_position]
        decipher_text += new_letter
    print(f"your decoded message is {decipher_text}")
    
   

def encrypt(message, shift):
    cipher_text = ""
    for letter in message:
      position=  alphabet.index(letter)  #to get the position of element of an list
      new_position = position + shift
      new_letter = alphabet[new_position]
      cipher_text +=new_letter
    print(f"the encoded text is {cipher_text}")

if direction == 'encode':
    encrypt(message ,shift)
    
    
if direction == 'decode':
    decrypt(message, shift)
    
    
    


