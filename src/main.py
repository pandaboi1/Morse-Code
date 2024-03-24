'''
Created By: Edwin Serna
Date Create: 03/24/2024
Date Edited: 03/24/2024 
'''
morse_code = { 
    'A' : '.-',    'B' : '-...',  'C' : '-.-.', 
    'D' : '-..',   'E' : '.',     'F' : '..-.', 
    'G' : '--.',   'H' : '....',  'I' : '..', 
    'J' : '.---',  'K' : '-.-',   'L' : '.-..', 
    'M' : '--',    'N' : '-.',    'O' : '---', 
    'P' : '.--.',  'Q' : '--.-',  'R' : '.-.', 
    'S' : '...',   'T' : '-',     'U' : '..-', 
    'V' : '...-',  'W' : '.--',   'X' : '-..-', 
    'Y' : '-.--',  'Z' : '--..',
    
    '1' : '.----', '2' : '..---',  '3' : '...--',
    '4' : '....-', '5' : '.....',  '6' : '-....',
    '7' : '--...', '8' : '---..',  '9' : '----.',
    '0' : '-----', 
    
    ',' : '--..--', '.' : '.-.-.-', '?' : '..--..', 
    '/' : '-..-.',  '-' : '-....-',  
    '(' : '-.--.',  ')' : '-.--.-' }

def encription(inputedMessage):
    encrypted = ''
    for letter in inputedMessage:
        if letter != morse_code[letter]:
            print("\nCharacter", morse_code[letter], "is not valid!")
            break
        if letter != ' ':
            encrypted += morse_code[letter]
        else:
            encrypted += ' '
    return encrypted    

message = input()
print(encription(message.upper()))