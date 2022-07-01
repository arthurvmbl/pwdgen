print("""
    
    
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
from itertools import permutations
from math import floor
def list_generator(list_of_possible_words,namelist,encode):
    if not encode:encode='utf-8'
    try:
        with open(namelist + ".txt",mode="wb") as f:
            list_of_possible_words = list(filter(None,list_of_possible_words))
            try:
                length = int(input(f"How many words do you want to combine? "))
                if length>len(list_of_possible_words):length = len(list_of_possible_words)
            except:length = len(list_of_possible_words)             
            for i in range(length,1,-1):
                try:
                    print('Permutation lenght: ',i)
                    permutation_examples = list(permutations(list_of_possible_words, length))
                    break
                except MemoryError as e:
                    print("Memory Error: ",e,'\nTrying to reduce the permutation lenght.')
                    permutation_examples = list()
            batch_size = 10000
            print(f'Batch size: '+str(batch_size)+' and '+str(len(permutation_examples))+' rows'  if batch_size<len(permutation_examples) else 'Batch size: '+str(len(permutation_examples)))
            last = floor(len(permutation_examples)/batch_size)
            for i in range(last):
                output = [(''.join(_)+'\n').encode(encode) for _ in permutation_examples[batch_size*i:batch_size*(i+1)]]
                f.writelines(output)
            output = [(''.join(_)+'\n').encode(encode) for _ in permutation_examples[batch_size*last:]]
            f.writelines(output)
        return True
    except:return False
if __name__=='__main__':
    namelist = input("Give your list a name: ")
    lista = 'Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua'.split(' ')
    
    encodings = ['unicode_escape','raw_unicode_escape','utf-8','ascii']
    for a,b in enumerate(encodings):print("",a,b,sep='\t')
    encode = input("\t>> ")
    try:encodings = encodings[int(encode)]
    except:encodings = None
    
    if list_generator(lista,namelist,encodings):
        print("Your list is ready!")
    else:
        print('Error on list creation.')