"""
Common functions
"""
from characterFunctions import character, inventory
import os

def pressEnter():
    raw_input('Press Enter to Continue')

def speech(text):
    print('')
    print(text)
    print('')

def displaySheet():
    for k, v in character.iteritems():
        print(k + ': ' + str(v))

def modGold(num):
    if num <= 0:
        inventory['Gold'] -= num
    else:
        inventory['Gold'] += num

def clearScreen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
