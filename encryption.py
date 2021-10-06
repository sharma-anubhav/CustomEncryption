###### README
'''
Make sure all the files (encryption.py,decryption.py,input.txt are in the same directory
The input.txt file will contain the text to be encrypted.
run the encryption.py file which will create 2 new files with level wise encrypted text.
once you have the encrypted text, you can run the decryption.pt to get the decrypted text.
'''
import binascii

def encrypt1(line):
    str = ""
    for word in line.split():

        key1 = len(word)
        for alphabet in word:
            new = ord(alphabet) + key1
            str = str + chr(new)
        str = str + " "
    #print(l1m)
    return str



def encrypt2(line):

    encryption_key = 232895080984906726156709911474167313427
    binary = ""
    for i in line:
        binary = binary + str(format(ord(i), 'b').zfill(32))
    i = 0
    crypt = ""
    while (len(crypt)<len(binary)):
        alphabet = binary[i:i + 128].zfill(128)
        new = int(alphabet, 2) ^ encryption_key
        crypt = crypt + str(format(new, 'b').zfill(128))
        i += 128
    return crypt

def decrypt1(line):
    str = ""
    for word in line.split():

        key1 = len(word)
        for alphabet in word:
            new = ord(alphabet) - key1
            if (new<0):
                new = 0
            str = str + chr(new)
        str = str + " "
    return str

def decrypt2(crypt):
    binary = ""
    for line in crypt:
        binary = binary + str(line)

    encryption_key = 232895080984906726156709911474167313427

    i = 0
    crypt = ""
    while (len(crypt)<len(binary)):
        alphabet = binary[i:i + 128]
        new = int(alphabet, 2) ^ encryption_key
        crypt = crypt + str(format(new, 'b').zfill(128))
        # print(chr(int(alphabet, 2)),end="")
        i += 128
    final = ""
    try:
        i = 0
        while (1):
            alphabet = crypt[i:i + 32]
            final = final + chr(int(alphabet, 2))
           # print(chr(int(alphabet, 2)), end="")
            i += 32
    except:
        pass
    return final

def remove_emptychar(line):
    for alpha in line:
        if alpha == chr(0):
            line = line.replace(chr(0), '')
    line = line.rstrip(" ")
    return line

if __name__ == "__main__":
    message = "hello this is anubhav sharma"
    print(message)
    print()
    level1_encryption = encrypt1(message)
    level1_encryption = level1_encryption.rstrip(" ")
    level2_encryption = encrypt2(level1_encryption)
    level2_decryption  = decrypt2(level2_encryption)
    level2_decryption = remove_emptychar(level2_decryption)
    original  = decrypt1(level2_decryption)
    print(original)


