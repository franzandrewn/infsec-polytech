import random

alphabet = []
for i in range(26):
    alphabet.append(chr(65 + i))
    alphabet.append(chr(97 + i))
for i in range(10):
    alphabet.append(chr(48 + i))
alphabet.append(',')
alphabet.append('.')

L = 7
password = ''
for i in range(L):
    password += random.choice(alphabet)
print("Your password:", password)