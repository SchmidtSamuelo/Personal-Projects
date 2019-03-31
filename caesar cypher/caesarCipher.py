# Take an array of the alphabet
# Shift it over by a user specified amount
# Encode the message
# Return encoded message
#
# Decoding:
# Take encoded message
# Allow user to change the key
# Return message decoded with user specified key

def encode():

    message = input("Please enter a message to encode: ").lower()
    cypherMessage = ''
    if any(i.isdigit() for i in message):
        return("please do not use any numbers in the message, only letters.")
    key = int(input("Please enter the key (1-26): "))
    if key > 26:
        print("Please only enter an integer between 1 and 26")

    for char in message:
        if char.isalpha:
            cypherChar = ord(char) + key
            if cypherChar > ord('z'):
                cypherChar -= 26
            cypherMessage += chr(cypherChar)
    print(cypherMessage)
    return cypherMessage

def decode():
    cypherMessage = input("please enter the encoded message: ").lower()
    key = int(input("please enter the key: "))
    message = ''

    if any(i.isdigit() for i in cypherMessage):
        return("please do not use any numbers in the message, only letters.")
    if key > 26:
        print("Please only enter an integer between 1 and 26")

    for char in cypherMessage:
        if char.isalpha:
            cypherChar = ord(char) - key
            if cypherChar < ord('z'):
                cypherChar += 26
            message += chr(cypherChar)
    print(message)
    return message