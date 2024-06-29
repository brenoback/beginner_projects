def madlib():
    print("######## Harry Potter Madlib ######## ")
    name = input("Name: ")
    adjective1 = input("Adjective: ")
    magical_creature = input("Magical Creature: ")
    spell = input("Spell: ")
    place = input("Place in Hogwarts: ")
    verb1 = input("Verb (Past Tense): ")
    adjective2 = input("Adjective: ")
    noun = input("Noun: ")
    verb2 = input("Verb (Present Tense): ")
    house = input("House at Hogwarts: ")


    madlib = f"{name} woke up feeling very {adjective1}. Today was going to be an exciting day at Hogwarts. \
As they were walking through the castle, they encountered a {magical_creature}. Remembering the {spell} spell they had learned in class, they cast it quickly. \
The spell worked perfectly, and the {magical_creature} led them to the {place} where a secret was hidden. They {verb1} the door and found a {adjective2} {noun} inside. \
They knew they had to {verb2} it back to their common room before anyone from {house} House found out."
    
    print(madlib)

