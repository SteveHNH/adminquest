"""
Common functions
"""
from __future__ import print_function
from characterFunctions import *
from questBoard import availableQuests
import os

def pressEnter():
    raw_input('Press Enter to Continue')

def speech(text):
    print('')
    print(text)
    print('')

def displaySheet():
    print('''
    Character Sheet
    ===============''')
    for key in character:
        print(key.title() + ': ' + str(character[key]).title())
    print('')

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

def mainTitle():
    print('''
    _       _           _        ___                  _
   / \   __| |_ __ ___ (_)_ __  / _ \ _   _  ___  ___| |_
  / _ \ / _` | '_ ` _ \| | '_ \| | | | | | |/ _ \/ __| __|
 / ___ \ (_| | | | | | | | | | | |_| | |_| |  __/\__ \ |_
/_/   \_\__,_|_| |_| |_|_|_| |_|\__\_\\__,_|\___||___/\__|
==========================================================
        A System Administration Learning Adventure
        ''')

def printQuests():
    print('''
          QUEST BOARD
          ===========
          ''')
    for k in availableQuests:
        print(k + ': ' + availableQuests[k])

def createChar(spec, speclist):
    character[spec] = ''
    while character[spec] == '':
        print
        print('Choose a ' + spec.title() + ':')
        for value in speclist:
            print(value.title())
        print('')
        print(spec.title() + ' Choice: ', end='')
        character[spec] = raw_input().lower()
        if character[spec] not in speclist:
            print('')
            print('Please choose a valid ' + spec)
            character[spec] = ''
        else:
            continue