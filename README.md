
# Custom Encryption Key

In cryptography, encryption is the process of encoding a message or information in a way that only authorized parties can access it and those who are not authorized cannot and similarly decryption is the method of decoding the encrypted information into its original/meaningful form and a key piece of information that determines the functional output of a cryptographic algorithm. For encryption algorithms, a key specifies the transformation of plaintext into ciphertext, and vice versa for decryption algorithms.<br>
Encryption (and decryption) algorithms are public knowledge, but it’s the key that makes them unique for each cryptosystem, and therefore, each communication.

Here we code a custom encryption method for implementation of a custom cryptography algorithm.

# Uniqueness

The basic idea behind our code is to define a key character for every character in the string based on its length and combining it with a 128-bit string of characters.<br>
Let’s dive a bit deeper into the working of the code with the help of an example illustrated through flowcharts.<br>
e.g. TEXT: “cyber”  <br>
Key1: 5 (Length of the string ‘cyber’)  <br>
128 bit encryption key: 232895080984906726156709911474167313427<br>

## The encryption algorithm thus created has a number of benefits which are as follows:

- The key used at level one is dynamic and this dynamic behaviour is achieved by changing the key value every time a new word is encountered which is difficult to detect and the brute force attack may fail. Adds great complexity.

- The second level of encryption uses a 128-bit key. For decrypting this, about 2128 attempts are required. To crack a 128-bit key by brute force will take around 500 billion years that is with one billion attempts per second. Thus with the current computational powers of computer systems it is nearly impossible to decrypt the message at level 2 of our cipher.


## Libraries Required
Whats brilliant is that this requires just 2 libraries
- Flask
-  Spacy

## Project Working
Step 1 of encryption involves processing the input word by word and using the length of that word as the key for implementing a shift-cipher. It has the benefit that same alphabets wont have the same cipher text and will be harder to break.
<br> In the next step we use the 128bit predefined key, which can be randomly generated and xor it with every 128bits of the Encryption 1 to get the final result. <br>. The Decryption processes are the reverse of these operations,
![enter image description here](https://github.com/sharma-anubhav/CustomEncryption/blob/master/data/1.png?raw=true)

![enter image description here](https://github.com/sharma-anubhav/CustomEncryption/blob/master/data/2.png?raw=true)

## Project Sample
### INPUT
![enter image description here](https://github.com/sharma-anubhav/CustomEncryption/blob/master/data/3.png?raw=true)

### OUTPUT

![enter image description here](https://github.com/sharma-anubhav/CustomEncryption/blob/master/data/4.png?raw=true)