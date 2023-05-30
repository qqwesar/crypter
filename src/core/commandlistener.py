from . import core

stages = ["INIT", "WORKING", "OFF"]
commands = ["setfile", "setout", "encryptcsr", "decryptcsr", "encryptvzr", "decryptvzr"]
class CommandListener:
    def __init__(self, stage: str) -> None:
        self.stage = stage
        self.command = "NULL"

    def start_listen(self):
        self.stage = stages[1]
        while True:
            self.command = input()
            if not self.command in commands:
                print("there is no such command!")

            else:
                if self.command in ["q", "exit", "stop"]:
                    self.stage = stages[2]
                    print("bye!")
                    break
                
                elif self.command == "setfile":
                    file_name = input("choose a file: ")
                    f = core.File(file_name)
                    print("file with name {} has set".format(file_name))

                elif self.command == "setout":
                    newname = input("choose new name of out.txt(WITH EXTENSION!!!): ")
                    f.change_out_name(newname)
                    print("out file name {} has set".format(newname))

                elif self.command == "encryptcsr":
                    key = input("set a key: ")
                    f.encrypt("csr", key)
                    print("csr encrypt completed\nwrote crypted data in {}".format(f.file_out))
                
                elif self.command == "decryptcsr":
                    key = input("enter a key: ")
                    f.decrypt("csr", key)
                    print("csr decrypt completed\nwrote encrypted data in {}".format(f.file_out))

                elif self.command == "encryptvzr":
                    key = input("enter a key: ")
                    f.encrypt("vzr", key)
                    print("vzr encrypt completed\nwrote encrypted data in {}".format(f.file_out))
                
                elif self.command == "decryptvzr":
                    key = input("enter a key: ")
                    f.decrypt("vzr", key)
                    print("vzr decrypt completed\nwrote decrypted data in {}".format(f.file_out))
