# BackTick v1.0.0
# https://github.com/SlashCreate/BackTick-for-python

import os
import time
from cmd import command

def clr():
  os.system('clr')
    
while True:
  a = input('>> ').split(' #')
  command(a[0], a)
  if a[0] == 'help':
    # help screen
    print('''
    help              help screen
    print #<text>     print <text> onto screen
    file.print #<f>   print contents of file <f>
    clr               clear screen
    exit              exit BackTick command line
    ''')
  elif a[0] == 'print':
    # print <text>
    print(a[1])
  elif a[0] == 'clr':
    clr()
  elif a[0] == 'file.print':
    read(a[1])
  elif a[0] == 'exit':
    clr()
    break
