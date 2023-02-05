# BackTick v1.0.0
# https://github.com/SlashCreate/BackTick-for-python

import os
import time

def clr():
  os.system('clr')
  
def command(cmd, args):
  # Use for custom commands
  # example:
  # custom #hello
  
  if cmd == 'custom':
    # args[0] is the same as command name
    print(args[1])
    
while True:
  a = input('>> ').split(' #')
  if a[0] == 'help':
    # help screen
    print('''
    help              help screen
    print #<text>     print <text> onto screen
    clr               clear screen
    exit              exit BackTick command line
    ''')
  elif a[0] == 'print':
    # print <text>
    print(a[1])
  elif a[0] == 'clr':
    clr()
  elif a[0] == 'exit':
    clr()
    break
