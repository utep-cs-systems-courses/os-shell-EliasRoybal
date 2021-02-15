import os, sys, re

def initialPrompt():
    while 1:
        prompt = os.write(1, ("$ ").encode())

        if 'PS1' in os.environ:
            prompt = os.environ['PS1']
        
        args = os.read(0, 10000)

        args = args.decode().lower().strip("\n")

        commandHandler(args)

def commandHandler(args):
    if args  == 'exit':
        sys.exit(0)
        
    else:
        print(args)

initialPrompt()
