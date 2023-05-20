import string

#one-letter substitution cipher
def crypt_csrch(data: str, key: int) -> str:
    data = data.lower()
    crypted_data = ""
    alphabet = list(string.ascii_lowercase)
    changed_alphabet = alphabet[-key:] + alphabet[:-key] #moving alphabet for [key] syllables right
    
    for i in range(len(data)):
        if data[i] in [" ", ".", ",", ":", "?", "!", "\n"]:
            crypted_data += data[i]
        else:
            crypted_data += changed_alphabet[alphabet.index(data[i])]
    return crypted_data

def encrypt_csrch(data: str, key: int) -> str:
    data = data.lower()
    encrypted_data = ""
    alphabet = list(string.ascii_lowercase)
    changed_alphabet = alphabet[-key:] + alphabet[:-key] #moving alphabet for [key] syllables right

    for i in range(len(data)):
        if data[i] in [" ", ".", ",", ":", "?", "!", "\n"]:
            encrypted_data += data[i]
        else:
            encrypted_data += alphabet[changed_alphabet.index(data[i])]
    return encrypted_data

#vizhener cipher

def crypt_vzrch(data: str, key: int) -> str:
    ...

def encrypt_vzrch(data: str, key: int) -> str:
    ...

