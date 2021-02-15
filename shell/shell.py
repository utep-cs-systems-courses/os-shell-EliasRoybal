import os, sys, re

def initialPrompt():
    while 1:
        os.write(1, ("$ ").encode())
        
        args = os.read(0, 10000)

        if args.decode().lower().strip("\n") == 'exit':
            sys.exit(0)
            
        else:
            print("input working")

initialPrompt()
