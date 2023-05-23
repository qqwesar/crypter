import random
import string

from . import crypt
#crypt method(changable)

class File:
    def __init__(self, file_in: str) -> None:
        self.file_out = "out.txt"
        with open(file_in, "r") as f: #getting file data from file_in which we need to crypt (in future mb)
            self.file_data = f.read()
        self.file_name = file_in
    
    def encrypt(self, method: str, key: str) -> None:
        if method == "csr":
            encrypted_data = crypt.encrypt_csrch(self.file_data, int(key))
            #creating keystring to decrypt message in future
            keystring = "".join([random.choice(string.ascii_lowercase) for i in range(int(key))])
            encrypted_data += f"\n{keystring}"
            with open(self.file_out, "w") as f:
                f.write(encrypted_data)
        elif method == "vzr":
            encrypted_data = crypt.encrypt_vzrch(self.file_data, key)
            #creating keystring to decrypt message in future
            keystring = key
            encrypted_data += f"\n{keystring}"
            with open(self.file_out, "w") as f:
                f.write(encrypted_data)
        else:
            pass

    def decrypt(self, method: str, key: int) -> None:
        if method == "csr":
            decrypted_data = crypt.decrypt_csrch(self.file_data, int(key))
            with open(self.file_out, "w") as f:
                f.write(decrypted_data)
        elif method == "vzr":
            decrypted_data = crypt.decrypt_vzrch(self.file_data, key)
            with open(self.file_out, "w") as f:
                f.write(decrypted_data)
        else:
            pass

    def change_out_name(self, new_name: str) -> None:
        self.file_out = new_name

    def get_file_data(self) -> str:
        return "File name: {}\nFile data:{}".format(self.file_name, self.file_data)
    
