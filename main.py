from src.core import commandlistener as cl

if __name__ == "__main__":
    cl = cl.CommandListener("INIT")

    cl.start_listen()    