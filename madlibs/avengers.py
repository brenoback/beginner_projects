def madlib():
    print("######## Avengers Madlib ######## ")
    superhero_name = input("Marvel Superhero Name: ")
    villain_name = input("Marvel Villain Name: ")
    place = input("Place: ")
    adjective1 = input("Adjective: ")
    noun = input("Noun: ")
    superpower = input("Superpower: ")
    verb1 = input("Verb (Past Tense): ")
    adjective2 = input("Adjective: ")
    verb2 = input("Verb: ")
    object_name = input("Object: ")






    madlib=f'{superhero_name} and the rest of the Avengers were preparing for their biggest mission yet. They had to stop the evil {villain_name} from destroying {place}. \
The situation was {adjective1}, and everyone was tense. Using their {noun}, {superhero_name} and the team strategized a plan. With the power of {superpower}, they {verb1} into action. \
The battle was {adjective2} and seemed endless. But when {superhero_name} managed to {verb2} the {object_name}, the tide of the battle turned in their favor. \
In the end, the Avengers saved the day and brought peace back to {place}.'

    print(madlib)


madlib()