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
    if inventory['Gold'] == 0 and num <= 0:
        print('You don\'t have any money to lose.')
    elif num <= 0:
        inventory['Gold'] -= num
    else:
        inventory['Gold'] += num

def clearScreen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def modXP(num):
    character['XP'] += num
