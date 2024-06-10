#the aim of this project is to use functions and loops to create a ceasar cypher

### --- IMPORTS --- ###

#import our logo
from art import logo
#import time for time.sleep
import time
#import os for clear
from os import system, name

### --- VARIABLE --- ###

#we want our alphabet here for choosing decode + encode letters, we include 2 copies so the shift number doesn't automatically error out if we put a letter
#near the end of the alphabet and it also enables us to use ridiculously sized shift numbers with modulo later
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

### --- FUNCS --- ###

#create our function it takes the message, encrypt amount and encrypt/ decrypt as args
def caesar(message, shift_amount, crypt):
    #if the encryption is decrypt, turn the number negative by * -1
    if crypt == 'decode':
        shift_amount = shift_amount * -1
    #variable for the encrypted/decrypted message
    new_message = ''
    #for loop for encryption
    for letter in message:
        #if the letter is in our alphabet (which it will be)
        if letter in alphabet:
            #go through the alphabet to find the index of the letter
            location = int(alphabet.index(letter))
            #add the shift amount to the index to get the new number
            new_position = location + shift_amount
            #new message += new letter
            new_message += alphabet[new_position]
        #if letter not in alphabet
        else:
            #add letter (this is for symbols ect)
            new_message += letter
        #print our new message
    print(f"Your encrypted/decrypted message is: {new_message}") 

# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

### --- MAIN --- ###

#log print and our inputs for user
print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#as stated before, we do 2 alphabets to ensure larger shift sizes and shifts with letters near the end of the alphabet
#eg z shift 1 would error out. The end result of two alphabets allows us to shift larger numbers. we do this by modulo-ing
#the number if it's larger than the alphabet. EG shift 27, would take the letter a all the way back to a and then +1 to b.
#instead of doing 3 4 or 5 alphabets we modulo the 27: 27%26, to get the 1 we would be moving anyway. 
if shift > 26:
    shift = shift % 26

#do function
caesar(message = text, shift_amount = shift, crypt = direction)
#setup new message variable
new_message = ''
#setup variable for while loop
go_again = True
#as we are not running any external files to save passwords we want to run a while loop to
#enable the user to keep encrypting/decrypting and testing without restarting the program
#and losing their current state
while go_again == True:
    #ask the user to try again
    Another_try = input("Would you like to go again Y or N?: ").lower()
    #if another try == yes
    if Another_try == 'y':
        #ask again and do function
        print(logo)
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n")) % 26    
        caesar(message = text, shift_amount = shift, crypt = direction)
    #finish code and clear
    else:
        print("Thank you for using the cypher, goodbye")
        go_again = False
        time.sleep(3)
        clear()