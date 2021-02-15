import os, sys, re

pid = os.getpid()

def initialPrompt():
    while True:
        currDirectoryPrompt = os.getcwd() +" $ " #includes current directory with '$'
        
        prompt = os.write(1, (currDirectoryPrompt).encode())

        if 'PS1' in os.environ:
            prompt = os.environ['PS1']
        
        args = os.read(0, 10000)

        args = args.decode().strip("\n").split()

        commandHandler(args)

def commandHandler(args):

    if len(args) == 0:
        pass
   
    elif args[0].lower() == 'exit':
        sys.exit(0)

    elif args[0].lower() == 'cd':
        try:
            os.chdir(args[1])
        except FileNotFoundError:
            print("No such directory founds")
        except IndexError: # no argument after 'cd'
            pass
        
    else:
        rc = os.fork()

        if rc < 0: #fork failed
            os.write(2, ("fork failed, returning %d\n" % rc).encode())
            return
        elif rc == 0:  # child
            os.write(1,"\n".encode())
            for dir in re.split(":", os.environ['PATH']): # try each directory in the path
                program = "%s/%s" % (dir, args[0])
                try:
                    os.execve(program, args, os.environ) # try to exec program
                except FileNotFoundError:             # ...expected
                    pass                              # ...fail quietly
                except Exception:
                    pass
            os.write(1, "Command not found\n".encode())
initialPrompt()
