# librarys your command(s) use:
import os

def command(cmd, args):
  # Use for custom commands
  # example:
  # custom #hello
  
  if cmd == 'custom':
    # args[0] is the same as command name
    print(args[1])

def read(file):
  myfile = open(file, "r")
  for line in myfile:
    print(line)
  myfile.close()

def setting():
  myfile = open(info/setting, "r")
  return myfile.read().split('\n')[0]
  myfile.close()
