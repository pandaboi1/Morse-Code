'''
Created By: Edwin Serna
Date Create: 03/24/2024
Date Edited: 03/24/2024 
'''
import mc_lib

# Validates the inputted message to make sure it can be encripted
def Validate(inputMessage):
    # Loops through inputted message one letter at a time to validate
    for letter in inputMessage: 
        x = 1
    return True


# Encrypts the inputted message from Morse Code dictionary
def Encript(inputMessage):
    encryptedMessage = ''
    
    # Loops through inputted message one letter at a time
    for letter in inputMessage: 
        # Checks key value pair from morse code dictionary 
        encryptedMessage += mc_lib.morse_code[letter]             
    return encryptedMessage   

def main():
    valid = False
    while not valid:
        message = input()
        valid = Validate(message)
        if ('')
        
    print(Encript(message))
        
if __name__ == '__main__':
 main()