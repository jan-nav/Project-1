"""
Project_1.py: První projekt v rámci Engeto Online Python Akademie

Author: Jan Navrátil
E-mail: navratill.jann@gmail.com
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

users = {'bob':'123', 
        'ann':'pass123', 
        'mike':'password123', 
        'liz':'pass123'}
separator = '-' * 30

login = input('Insert name: ')
password = input('Insert password: ')
if login not in users.keys() or password != users[login]:                                           # Hlavní podmínka celého programu: kontrola vstupních přihlašovacích údajů s uloženými
    print('Incorrect login credentials! Terminating the program...')
    
else:
    print(separator, f'Welcome to the text analyzer, {login}',
        'There are 3 texts ready for analysis.', separator, sep='\n')
    text_num = input('Please select a number between 1-3 to select a text: ')
    print(separator)
    if not text_num.isnumeric():                                                                    # Výběr textu s kontrolou vstupních údajů
        print('Invalid input! (Numbers only). Terminating the program...')
    elif int(text_num) not in tuple(range(1,4)):
        print('Invalid input! (Out of defined range). Terminating the program...')
    else:
        text_select = TEXTS[int(text_num)-1]
        word_list = []
        num_list = []
        word_count = int()
        word_cap_count = int()                                                                      # Definice proměnných použitých k počítání statistických údajů
        word_upp_count = int()
        word_low_count = int()
        num_count = int()
        word_len = {}

        for word in text_select.split():                                                            # Počítání celkového počtu slov
            word_count = word_count + 1                                                             
            if word.istitle():                                                                      # Počítání slov začínajících velkým písmenem
                word_cap_count = word_cap_count + 1                                                 
            if word.isupper() and word.isalpha():                                                   # Počítání slov psaných velkými písmeny s kontrolou, zda string neobsahuje čísla 
                word_upp_count = word_upp_count + 1                                                 
            if word.islower():                                                                      # Počítání slov psaných malými písmeny
                word_low_count = word_low_count + 1
            if word.isnumeric():                                                                    # Počítání čísel a vkládání jejich hodnot do slovníku za účelem výpočtu celkové sumy
                num_count = num_count + 1
                num_list.append(int(word))
            word_list.append(word.strip(",.:;!?").lower())                                          # Vkládání očištěných slov do seznamu za účelem výpočtu množství znaků pro jednotlivá slova

        total = sum(tuple(num_list))                                                                # Součet čísel
        for word in word_list:                                                                      # Počítání znaků v jednotlivých slovech a vkládání jednotlivých hodnot do slovníku
            lett_count = len(word)
            if lett_count not in word_len:
                word_len[lett_count] = 1
            else:
                word_len[lett_count] = word_len[lett_count] + 1
        keys = list(word_len.keys())                                                                # Převedení slovníkových klíčů, obsahujících jednotlivé počty znaků, do seznamu
        keys.sort()                                                                                 # Seřazení hodnot za účelem vypisování ve vzestupném pořadí
        
        print(f'There are {word_count} words in the text.',                                         # Zobrazení konečných hodnot
              f'There are {word_cap_count} titlecase words.',
              f'There are {word_upp_count} uppercase words.',
              f'There are {word_low_count} lowercase words.',
              f'There are {num_count} numeric strings.',
              f'The sum of all the numbers is {total}.',
              separator, sep='\n')
        print('{}{:^20}{}'.format('LEN|', 'OCCURENCES', '|NR.'), separator, sep='\n')               # Zobrazení hodnot ve sloupcovém grafu
        for key in keys:
            print('{:>4}{:<20}{}'.format(f'{key}|', '*' * word_len.get(key), f'|{word_len.get(key)}'))    