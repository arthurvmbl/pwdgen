from itertools import permutations
from math import floor

def list_generator(file_name, namelist, encode):
    if not encode:
        encode = 'utf-8'
    try:
        with open(file_name, mode="r", encoding=encode) as file:
            lines = file.readlines()
            lista = [word.strip() for line in lines for word in line.split()]

        with open(namelist + ".txt", mode="wb") as f:
            lista = list(filter(None, lista))
            try:
                length = int(input(f"How many words do you want to combine? "))
                if length > len(lista):
                    length = len(lista)
            except:
                length = len(lista)
            for i in range(length, 1, -1):
                try:
                    print('Permutation length:', i)
                    permutation_examples = list(permutations(lista, length))
                    break
                except MemoryError as e:
                    print("Memory Error:", e, '\nTrying to reduce the permutation length.')
                    permutation_examples = list()
            batch_size = 10000
            print(f'Batch size: {batch_size} and {len(permutation_examples)} rows' if batch_size < len(permutation_examples) else f'Batch size: {len(permutation_examples)}')
            last = floor(len(permutation_examples) / batch_size)
            for i in range(last):
                output = [(''.join(_)+'\n').encode(encode) for _ in permutation_examples[batch_size*i:batch_size*(i+1)]]
                f.writelines(output)
            output = [(''.join(_)+'\n').encode(encode) for _ in permutation_examples[batch_size*last:]]
            f.writelines(output)
        return True
    except:
        return False

if __name__ == '__main__':
    namelist = input("Give your list a name: ")
    file_name = input("Enter the file name: ")  # Input the file name containing the words
    encodings = ['unicode_escape', 'raw_unicode_escape', 'utf-8', 'ascii']
    for a, b in enumerate(encodings):
        print("", a, b, sep='\t')
    encode = input("\t>> ")
    try:
        encodings = encodings[int(encode)]
    except:
        encodings = None

    if list_generator(file_name, namelist, encodings):
        print("Your list is ready!")
    else:
        print('Error on list creation.')
