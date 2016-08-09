'''
Adminquest
==========
This is a basic framework for how adminquest is going to work. I have mostly no
idea what I'm doing yet, but I'm kind of excited about the possibilities.
'''

from __future__ import print_function
from questBoard import availableQuests
from characterFunctions import inventory, character, availableRaces, availableClasses
from functions import pressEnter, speech, modGold, displaySheet, clearScreen

def printQuests():
    print('''
          QUEST BOARD
          ===========
          ''')
    for k in availableQuests:
        print(k + ': ' + availableQuests[k])

print('''
                 ADMINQUEST
                 ==========
       A Sysadmin Learning Adventure!
       ''')

print('What is your name, Adventurer? ')
character['NAME'] = raw_input()

speech('''
It is so good to see you, ''' + character['NAME'] + '!' + '''
My vision is poor, my friend. It has been a long time since an adventurer
such as yourself has made their way to this place.''')

pressEnter()
clearScreen()
speech('''
Tell me, ''' + character['NAME'] + ', of what race are you?')
while character['RACE'] == '':
    print
    print('Choose a Race:')
    for race in availableRaces:
        print(race)
    print('')
    print('Race Choice: ', end='')
    character['RACE'] = raw_input()
    if character['RACE'] not in availableRaces:
        print('')
        print('Please choose a valid race')
        character['RACE'] = ''
    else:
        continue

print('')
if character['RACE'] == 'Elf':
    print('Oh, so you\'re an ' + str.lower(character['RACE']) +
          ', eh? Excellent')
else:
    print('Oh, so you\'re a ' + str.lower(character['RACE']) +
          ', eh? Excellent')
print('')

pressEnter()
clearScreen()
speech('''You clearly have seen a bit of the world. What would you say you specialize
in, friend? What is your profession?''')

while character['CLASS'] == '':
    print('Choose a Class')
    for classes in availableClasses:
        print(classes)
    print('')
    print('Class Choice: ')
    character['CLASS'] = raw_input()
    if character['CLASS'] not in availableClasses:
        print('')
        print('Please choose a valid class')
        character['CLASS'] = ''
    else:
        continue

speech('Fantastic! We need more ' + str.lower(character['CLASS']) +
      's in the world')

pressEnter()
clearScreen()

speech('Well, ' + character['NAME'] + ', we have a lot of work to do.')
speech('''
The system is broken, friend. We need a system administrator to help bring
it back. But first, you'll need some training. Here I have a list of "quests"
that you can undertake to hone your skills. Choose them wisely, and good
luck!''')

modGold(50)
speech('Oh! By the way, here\'s ' + str(inventory['Gold']) +
      ' gold to get you started')

pressEnter()
clearScreen()
speech('One more thing, ' +character['NAME'] + '.')
pressEnter()
speech('It\'s dangerous to go alone. Take this!')
inventory['Mainhand'] = 'Wooden Stick'
speech('Received: ' + inventory['Mainhand'])
pressEnter()

displaySheet()
printQuests()
