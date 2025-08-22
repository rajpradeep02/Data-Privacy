
# Write a Python program that generates a password 
# using a random combination of words from a dictionary file.

import random

dict = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k',
        11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u',
        21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z', 26: 'A', 27: 'B', 28: 'C', 29: 'D', 30: 'E',
        31: 'F', 32: 'G', 33: 'H', 34: 'I', 35: 'J', 36: 'K', 37: 'L', 38: 'M', 39: 'N', 40: 'O',
        41: 'P', 42: 'Q', 43: 'R', 44: 'S', 45: 'T', 46: 'U', 47: 'V', 48: 'W', 49: 'X', 50: 'Y',
        51: 'Z', 52: '0', 53: '1', 54: '2', 55: '3', 56: '4', 57: '5', 58: '6', 59: '7', 60: '8',
        61: '9', 62: '!', 63: '*', 64: '#', 65: '$', 66: '%', 67: '&', 68: "@", 69: '^', 70: '?'}

def randomPassword(length = 8):
    sample = random.sample(list(dict),length)
    password = "".join(dict[key] for key in sample)
    return password

if __name__ == "__main__":
    length = int(input("Enter Length of your Password: "))
    print("Suggested Password is: ",randomPassword(length))
