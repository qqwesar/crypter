from src.core import core

if __name__ == "__main__":
    while True:
        command = input()

        if command in ["q", "exit", "stop"]:
            break

        elif command == "setfile":
            file_name = input("choose a file: ")
            f = core.File(file_name)

        elif command == "setout":
            newname = input("choose new name of out.txt(WITH EXTENSION!!!): ")
            f.change_out_name(newname)

        elif command == "cryptcsr":
            key = int(input("set a key: "))
            f.crypt("csr", key)
            print("csr crypt completed\nwrote crypted data in {}".format(f.file_out))
        
        elif command == "encryptcsr":
            key = int(input("enter a key: "))
            f.encrypt("csr", key)
            print("csr encrypt completed\nwrote encrypted data in {}".format(f.file_out))
            