from itertools import permutations
def list_generator(list_of_possible_words,namelist):
    try:
        with open(namelist + ".txt",mode="wb") as f:
            list_of_possible_words = list(filter(None,list_of_possible_words))
            length = int(input(f"How many words do you want to combine? "))
            permutation_examples = list(permutations(list_of_possible_words, length))
            output = [(''.join(_)+'\n').encode() for _ in permutation_examples]
            f.writelines(output)
        return True
    except:return False
print("""\
    
    
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@                                                                                                                                             @@@@@
@@@@  @@@@@@@@@@@@@        @@@@@@@@@@@      @@@@       @@@@    @@@@@@@@@@@@               @@@@@@@@@@@      @@@@@@@@@@@@@@@    @@@@       @@@@    @@@@@
@@@@  @@@@       @@@@    @@@@               @@@@       @@@@    @@@@       @@@           @@@@               @@@@               @@@@@@@@@  @@@@    @@@@@
@@@@  @@@@       @@@@      @@@@@@@@@@@      @@@@   @@  @@@@    @@@@       @@@@  @@@@@@  @@@@     @@@@@@    @@@@@@@@@@@@@      @@@@   @@@@@@@@    @@@@@
@@@@  @@@@@@@@@@@@@                 @@@@    @@@@@@@@@@@@@@@    @@@@       @@@@  @@@@@@  @@@@       @@@@    @@@@               @@@@     @@@@@@    @@@@@
@@@@  @@@@               @@@@       @@@@    @@@@@@   @@@@@@    @@@@     @@@@            @@@@       @@@@    @@@@               @@@@       @@@@    @@@@@
@@@@  @@@@                 @@@@@@@@@@@      @@@@       @@@@    @@@@@@@@@@@                @@@@@@@@@@  @    @@@@@@@@@@@@@@@    @@@@       @@@@    @@@@@
@@@@                                                                                                                                             @@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

by arthurvmbl & HenriqueMenezesN   

    """)


namelist = input("Give your list a name: ")
f = open(namelist + ".txt","w+")
name = input("Name; ")
nick = input("Nickname; ")
yearbirth = input("Year of Birth; ")
relative1 = input("Relative; ")
relative2 = input("Relative; ")
relative3 = input("Relative; ")
relative4 = input("Relative; ")
favoriteword = input("Favorite Word: ")
id = input("Id: ")
phone = input("Phone; ")
oldphone = input("Old Phone; ")
ss = input("Personal Doc: ")
dobw = input("Year of Birth of Spouse; ")
pet = input("Pet; ")
job = input("Job; ")
team = input("Team/Sport; ")

lista = [name, nick, yearbirth, relative1, relative2, relative3, relative4, favoriteword, phone,
             oldphone, id, ss, dobw, pet, job, team]

list_generator(lista,namelist)    
print("Your list is ready!")