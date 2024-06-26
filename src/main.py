'''
Created By: Edwin Serna
Date Create: 03/24/2024
Date Edited: 03/28/2024 
'''
import mc_lib
import sys
import time


# Validates the inputted message to make sure it can be encripted
def isValid(inLetter):
    # Loops to Validate each letter
    if inLetter.upper() not in mc_lib.morse_code and inLetter != ' ':
        return False
    return True

# Encrypts the inputted message from Morse Code dictionary
def Encrypt(inLetter):
    if not isValid(inLetter):
        return "Not valid input!!!"
    
    encryptedLetters = ""
    # Checks key value pair from morse code dictionary 
    encryptedLetters += mc_lib.morse_code.get(inLetter.upper(), "") + " "     
    #.strip() # Removes leading/tailing whitespace
    return encryptedLetters

def main():
    Encrypted_message = ""
    print("Input your message:\n\t")
    while True:
        # Read a single character from standard input without waiting for enter
        letter = sys.stdin.read(1)
        
        # Check if the character is a newline character, indicating end of input
        if letter == '\n' or letter.lower == "exit":
            break
        
        # Add the character to the user_input string
        Encrypted_message += Encrypt(letter) + " "
        
        # Output the current input
        sys.stdout.write("\r\t" + Encrypted_message)
        sys.stdout.flush()
        
        # You can add some delay if needed
        time.sleep(0.5)
    
    print("\n\nEncrypted Message Is: \n\n\t", Encrypted_message.strip(), "\n")
        
# -----------------------------------------
if __name__ == '__main__':
    main()