import itertools

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

lista = list(filter(None, lista))
    
print(len(lista))

tamain = int(input("How many words do you want to combine? "))

s = lista
t = list(itertools.permutations(s, tamain))
for i in range(0, len(t)):
        print(''.join(t[i]), file=f)
    
print("Your list is ready!")