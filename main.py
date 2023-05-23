from src.core import core

if __name__ == "__main__":
    while True:
        command = input()

        if command in ["q", "exit", "stop"]:
            print("bye!")
            break

        elif command == "setfile":
            file_name = input("choose a file: ")
            f = core.File(file_name)
            print("file with name {} has set".format(file_name))

        elif command == "setout":
            newname = input("choose new name of out.txt(WITH EXTENSION!!!): ")
            f.change_out_name(newname)
            print("out file name {} has set".format(newname))

        elif command == "encryptcsr":
            key = input("set a key: ")
            f.encrypt("csr", key)
            print("csr encrypt completed\nwrote crypted data in {}".format(f.file_out))
        
        elif command == "decryptcsr":
            key = input("enter a key: ")
            f.decrypt("csr", key)
            print("csr decrypt completed\nwrote encrypted data in {}".format(f.file_out))

        elif command == "encryptvzr":
            key = input("enter a key: ")
            f.encrypt("vzr", key)
            print("vzr encrypt completed\nwrote encrypted data in {}".format(f.file_out))
        
        elif command == "decryptvzr":
            key = input("enter a key: ")
            f.decrypt("vzr", key)
            print("vzr decrypt completed\nwrote decrypted data in {}".format(f.file_out))