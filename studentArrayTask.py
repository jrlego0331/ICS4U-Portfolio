characters = [('Eric', 'Cartman', 'Red', 0.0, 'Fatass'),
              ('Stan', 'Marsh', 'Blue', 1.0, 'Hippie'),
              ('Kyle', 'Broflovski', 'Green', 1.0, 'Ginger'),
              ('Kenney', 'McCormick', 'Orange', 2.0, 'Poor')]
attributes = ('first name', 'last name', 'main color', 'number of siblings', 'nickname')
alphabets = ('A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i',
            'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r',
            'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'S', 's', 'Y', 'y', 'Z', 'z')

def displayArray(array):
    print('-'*60)
    for item in array:
        print(item[0], item[1], 'wears', item[2], 'and has', item[3], 'siblings. He is the', item[4])
    print('-'*60)
    

while True:
    displayArray(characters)

    try: operation = int(input('1 - add item\t2 - delete item\t3 - sort\t4 - quit'))
    except: 
        print('wrong input')
        operation = 0
    
    #item adding
    if operation == 1: 
        print('adding new chracter')
        newItem = list(input('input firstname, lastname, main color, number of siblings and nickname, distinguish by space').split(' '))
        if len(newItem) == 5:
            newItem[3] = float(newItem[3])
            characters.append(newItem)
            continue
        print('missing componet!')

    #item deleting
    if operation == 2:
        delWhat = input('character with specific attribute you inputed will be deleted')
        for item in characters:
            for component in item:
                if component == delWhat: characters.pop(characters.index(item))

    #item sorting
    if operation == 3:
        print('sorting selected. sort by:')
        sortBy = attributes.index((input(attributes)))
        order = []
        rcChanged = list(zip(*characters))
        newlist = []

        if sortBy != 3:
            for n in range(len(rcChanged[sortBy])):
                try:
                    obsAlphabetIndex = alphabets.index(rcChanged[sortBy][n][0])
                    dupleIndex = order.index(obsAlphabetIndex) 
                    if alphabets.index(rcChanged[sortBy][n][1]) > alphabets.index(rcChanged[sortBy][dupleIndex][1]): order.append(obsAlphabetIndex+0.5)
                    else: order.append(obsAlphabetIndex-0.5)

                except: order.append(alphabets.index(rcChanged[sortBy][n][0]))
            
        else: order = list(rcChanged[sortBy])
        
        for n in range(len(order)):
            indexOfMax = order.index(min(order))
            newlist.append(characters[indexOfMax])
            order[indexOfMax] = 100.0
        
        characters = newlist
       
    #quit
    if operation == 4: break
