'''
Adminquest
==========
This is a basic framework for how adminquest is going to work. I have mostly no
idea what I'm doing yet, but I'm kind of excited about the possibilities.
'''

from __future__ import print_function
from questBoard import availableQuests
from dataStore import inventory, character, availableRaces, availableClasses
from functions import *

clearScreen()
mainTitle()

raw_input('''
Press Enter to Begin Your Quest...
''')

print('What is your name, Adventurer? ')
character['name'] = raw_input()

speech('''
It is so good to see you, ''' + character['name'].title() + '!' + '''
My vision is poor, my friend. It has been a long time since an adventurer
such as yourself has made their way to this place.''')

pressEnter()
clearScreen()
speech('''
Tell me, ''' + character['name'] + ', of what race are you?')
createChar('race', availableRaces)

print('')
if character['race'].lower() == 'elf':
    print('Oh, so you\'re an ' + str.lower(character['race']) +
          ', eh? Excellent')
else:
    print('Oh, so you\'re a ' + str.lower(character['race']) +
          ', eh? Excellent')
print('')

pressEnter()
clearScreen()
speech('''You clearly have seen a bit of the world. What would you say you specialize
in, friend? What is your profession?''')

createChar('class', availableClasses)

speech('Fantastic! We need more ' + str.lower(character['class']) +
      's in the world')

pressEnter()
clearScreen()

speech('Well, ' + character['name'] + ', we have a lot of work to do.')
speech('''
The system is broken, friend. We need a system administrator to help bring
it back. But first, you'll need some training. Here I have a list of "quests"
that you can undertake to hone your skills. Choose them wisely, and good
luck!''')

modGold(50)
speech('Oh! By the way, here\'s **' + str(inventory['Gold']) +
      '** gold to get you started')

pressEnter()
clearScreen()
speech('Makes sure I got all your details correct')
displaySheet()

speech('Would you like to change anything? (y/n) ')
sheetChange = raw_input()
if sheetChange.lower() == 'y':
    while sheetChange.lower() == 'y':
        speech('What would you like to change?')
        print('Name, Class, or Race: ', end='')
        choice = raw_input()
        if choice.lower() == 'name':
            speech('What would you like to change your name to?')
            character['name'] = ''
            while character['name'] == '':
                newName = raw_input()
                character['name'] = newName.title()
            displaySheet()
            print('Would you like to change anything else? (y/n) ', end='')
            answer = raw_input()
            if answer.lower() == 'n':
                sheetChange = 'n'
        elif choice.lower() == 'class':
            speech('What would you like to change your class to? ')
            character['class'] = ''
            createChar('class', availableClasses)
            displaySheet()
            print('Would you like to change anything else? (y/n) ', end='')
            answer = raw_input()
            if answer.lower() == 'n':
                sheetChange = 'n'
        elif choice.lower() == 'race':
            speech('What would you like to change your race to?')
            character['race'] = ''
            createChar('race', availableRaces)
            displaySheet()
            print('Would you like to change anything else? (y/n) ', end='')
            answer = raw_input()
            if answer.lower() == 'n':
                sheetChange = 'n'
        else:
            print('If you want to change something, do it.')


speech('One more thing, ' +character['name'] + '.')
pressEnter()
clearScreen()
speech('It\'s dangerous to go alone. Take this!')
inventory['Mainhand'] = 'Wooden Stick'
speech('Received: ' + inventory['Mainhand'])
pressEnter()
clearScreen()

mainTitle()
mainMenu()
