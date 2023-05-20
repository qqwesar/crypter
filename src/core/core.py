from . import crypt #crypt method(changable)

class File:
    def __init__(self, file_in: str) -> None:
        self.file_out = "out.txt"
        with open(file_in, "r") as f: #getting file data from file_in which we need to crypt (in future mb)
            self.file_data = f.read()
        self.file_name = file_in
    
    def crypt(self, method: str, key: int) -> None:
        if method == "csr":
            crypted_data = crypt.crypt_csrch(self.file_data, key)
            with open(self.file_out, "w") as f:
                f.write(crypted_data)
        elif method == "vzr":
            pass #todo: vizhener crypt
        else:
            pass
        
    def encrypt(self, method: str, key: int) -> None:
        if method == "csr":
            encrypted_data = crypt.encrypt_csrch(self.file_data, key)
            with open(self.file_out, "w") as f:
                f.write(encrypted_data)
        elif method == "vzr":
            pass #todo: vizhener encrypt
        else:
            pass

    def change_out_name(self, new_name: str) -> None:
        self.file_out = new_name

    def get_file_data(self) -> str:
        return "File name: {}\nFile data:{}".format(self.file_name, self.file_data)
    
