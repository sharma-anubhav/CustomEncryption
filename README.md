
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

The flask project can be downloaded and run on a local host.
Also .exe and .dmg files for the application are provided so that the application directly runs without the need for installing any dependancies.


## Project Sample
![enter image description here](https://github.com/sharma-anubhav/blog/blob/master/img/CV_AI.jpg?raw=true)
