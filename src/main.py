'''
Created By: Edwin Serna
Date Create: 03/24/2024
Date Edited: 03/24/2024 
'''
import mc_lib

def encription(inputedMessage):
    encrypted = ''
    for letter in inputedMessage:
        if letter != ' ':
            encrypted += mc_lib.morse_code[letter]
        else:
            encrypted += ' '
    return encrypted    

def main():
        message = input()
        print(encription(message.upper()))
        
if __name__ == '__main__':
 main()