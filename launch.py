'''
Adminquest
==========
This is a basic framework for how adminquest is going to work. I have mostly no
idea what I'm doing yet, but I'm kind of excited about the possibilities.
'''

from __future__ import print_function
from questBoard import availableQuests


def printQuests():
    print('''
          QUEST BOARD
          ===========
          ''')
    for k in availableQuests:
        print(k + ': ' + availableQuests[k])


inventory = {'Gold': 50,
             'Head': '',
             'Chest': '',
             'Hands': '',
             'Legs': '',
             'Feet': '',
             'Shoulders': '',
             'Slot 1': '',
             'Slot 2': '',
             'Slot 3': '',
             'Slot 4': '',
             'Slot 5': '',
             'Slot 6': '',
             'Slot 7': '',
             'Slot 8': '',
             'Slot 9': ''}

character = {'NAME': '',
             'RACE': '',
             'CLASS': '',
             'XP': 0}

availableRaces = ['Human', 'Elf', 'Dwarf', 'Halfling']
availableClasses = ['Warrior', 'Rogue', 'Mage']

print('''
                 ADMINQUEST
                 ==========
       A Sysadmin Learning Adventure!
       ''')

print('What is your name, Adventurer? ')
character['NAME'] = raw_input()

print('''
It is so good to see you, ''' + character['NAME'] + '!' + '''
My vision is poor, my friend. It has been a long time since an adventurer
such as yourself has made their way to this place.

Tell me, ''' + character['NAME'] + ', of what race are you?')
print('')

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

raw_input('Press Enter to Continue...')

print('')
print('''
You clearly have seen a bit of the world. What would you say you specialize
in, friend? What is your profession?
''')

while character['CLASS'] == '':
    print('')
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

print('')
print('Fantastic! We need more ' + str.lower(character['CLASS']) +
      's in the world')

print('')

raw_input('Press Enter to Continue...')

print('')
print('Well, ' + character['NAME'] + ', we have a lot of work to do.')
print('')
print('''
The system is broken, friend. We need a system administrator to help bring
it back. But first, you'll need some training. Here I have a list of "quests"
that you can undertake to hone your skills. Choose them wisely, and good
luck!''')

print('')
print('Oh! By the way, here\'s ' + str(inventory['Gold']) +
      ' gold to get you started')

print('')
printQuests()
