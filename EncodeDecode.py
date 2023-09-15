#Encoding -
# if word =3 or >3 then remove first letter and append at end then add 3 random characters at beginning and at end
# else reverse the string

#Decoding - 
# if word<3 then reverse it
# else remove 3 characters from start and end then remove last character an dplace in beginning  
import random
import string


def encode(word):
    length = len(word)
    if(length<3):
        new_encode = word[::-1]
        return new_encode
    else:
        temp = word[1:length]
        temp += word[0]
        for i in range(6):
            if(i<3):
                random_letter = random.choice(string.ascii_letters)
                temp = random_letter + temp
            else:
                random_letter = random.choice(string.ascii_letters)
                temp = temp + random_letter
        return temp

def decode(encoded):
    length = len(encoded)
    if(length<3):
        new_decode = encoded[::-1]
        return new_decode
    else:
        temp = encoded[3:length]
        temp = temp[::-1]
        temp = temp[3:len(temp)]
        new_decode = temp[1:len(temp)]+temp[0]
        new_decode = new_decode[::-1]
        return new_decode

word = input("Enter the word: ")
encoded = encode(word)
print(encoded)
decoded = decode(encoded)
print(decoded)
