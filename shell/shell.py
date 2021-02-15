import os, sys, re

def initialPrompt():
    while 1:
        currDirectoryPrompt = os.getcwd() +" $ " #includes current directory with '$'
        
        prompt = os.write(1, (currDirectoryPrompt).encode())

        if 'PS1' in os.environ:
            prompt = os.environ['PS1']
        
        args = os.read(0, 10000)

        args = args.decode().strip("\n").split()

        commandHandler(args)

def commandHandler(args):
    currDirectory = os.getcwd()
    
    if args[0].lower() == 'exit':
        sys.exit(0)

    elif args[0].lower() == 'cd':
        try:
            os.chdir(args[1])
        except FileNotFoundError:
            print("No such directory found")
        except IndexError: # no argument after 'cd'
            os.chdir(currDirectory)
        
    else:
        print(args)

initialPrompt()
