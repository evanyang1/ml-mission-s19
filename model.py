#import keras as keras

encrypted = open("encrypted.txt", "r")
encryptedWords = (encrypted.read()).split()

decrypted = open("decrypted.txt", "r")
decryptedWords = (decrypted.read()).split()

print(encryptedWords)
print(decryptedWords)
