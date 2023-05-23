import string

#one-letter substitution cipher
def encrypt_csrch(data: str, key: int) -> str:
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

def decrypt_csrch(data: str, key: int) -> str:
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

def encrypt_vzrch(message: str, key: str) -> str:
    message = message.upper()
    encrypted_message = ''
    key = key.upper().replace(' ', '')
    key_len = len(key)

    for i in range(len(message)):
        char = message[i]

        if not char.isalpha():
            encrypted_message += char
            continue

        # symb num in alphabet
        char_index = ord(char.upper()) - ord('A')

        # key symb num in alphabet
        key_index = ord(key[i % key_len].upper()) - ord('A')

        # encrypted symb num in alphabet
        new_char_index = (char_index + key_index) % 26

        encrypted_message += chr(new_char_index + ord('A'))

    return encrypted_message

def decrypt_vzrch(data: str, key: str) -> str:
    key = key.upper()
    key_len = len(key)
    key_as_int = [ord(i) for i in key]
    msg_as_int = [ord(i) for i in data]

    decrypted = []
    for i in range(len(data)):
        if data[i] in [" ", ".", ",", ":", "?", "!", "\n"]:
            decrypted.append(data[i])
        else:
            decrypted.append(chr((msg_as_int[i] - key_as_int[i % key_len]) % 26 + ord('A')))

    return ''.join(decrypted)