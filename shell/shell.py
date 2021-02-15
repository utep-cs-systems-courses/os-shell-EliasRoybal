import os, sys, re

def initialPrompt():
    while 1:
        args = input("$ ")

        if args == "exit":
            sys.exit(0)

        else:
            print("input working")

initialPrompt()
