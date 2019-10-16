import os,json,copy
from Chain import Chain

color = {
   "LBLUE" : '\033[94m',
   "LGREEN" : '\033[92m',
   "LYELLOW" : '\033[93m',
   "LRED" : '\033[91m',
   "BLUE" : '\033[34m',
   "YELLOW" : '\033[33m',
   "RED" : '\033[31m',
   "GREEN" : '\033[32m',
   "PURPLE" : '\033[35m',
   "ENDC" : '\033[0m'
}

def select(index):
    index = index - 1
    while True:
        os.system('clear')
        print(color['BLUE'] + "[PyBlock:Chains:" + chains[index].name + "]" + color['ENDC'])
        print()
        print(color['LGREEN'] + "1." + color['ENDC'] + "Add New Block")
        print(color['LGREEN'] + "2." + color['ENDC'] + "Delete Last Block")
        print(color['LGREEN'] + "3." + color['ENDC'] + "Verify Chain")
        print(color['LGREEN'] + "4." + color['ENDC'] + "Delete Chain")
        print(color['LRED'] + "0." + color['ENDC'] + "Back")
        print()
        c = int(input(color['LGREEN'] + ">" + color['ENDC']))
        if c == 1:
            data = input("Data" + color['LGREEN'] + ">" + color['ENDC'])
            chains[index].add(data)
            save()
        elif c == 2:
            if len(chains[index].blocks) > 1:
                del chains[index].blocks[-1]
            else:
                 print(color['LRED'] + 'Cant Delete Genesis Block' + color['ENDC'])
            save()
        elif c == 3:
                chains[index].verify(True)
        elif c == 4:
            del chains[index]
            save()
        elif c == 0:
            return
        else:
            continue

def save():
    save_chain = []
    for index, chain in enumerate(chains):
        save_dicts = copy.deepcopy(chain.__dict__)
        save_block = []
        for block in chain.blocks:
            save_block.append(block.__dict__)
        save_dicts['blocks'] = save_block
        save_chain.append(save_dicts)
    file = open('chains', 'w')
    file.write(json.dumps(save_chain))
    file.close()

if __name__ == "__main__":
    chains = []
    try:
        while True:
            os.system('clear')
            print(color['BLUE'] + "[PyBlock]" + color['ENDC'])
            print()
            print(color['LGREEN'] + "1." + color['ENDC'] + "Select Chain")
            print(color['LGREEN'] + "2." + color['ENDC'] + "New Chain")
            print(color['LRED'] + "0." + color['ENDC'] + "Exit")
            print()
            try:
                choice = int(input(color['LGREEN'] + ">" + color['ENDC']))
                if choice > 2 or choice < 0:
                    raise Exception("Number Out Of Menu Range")
            except ValueError:
                print(color['LRED'] + 'Please Enter A Valid Number' + color['ENDC'])
            except Exception as e:
                print(color['LRED'] + 'Number Out Of Menu Range, Please Enter A Valid Number' + color['ENDC'])
            print()
            if choice == 0:
                break
            elif choice == 1:
                os.system('clear')
                print(color['BLUE'] + "[PyBlock:Chains]" + color['ENDC'])
                print()
                for index, chain in enumerate(chains):
                    print(color['LYELLOW'] + str(index + 1) + "." + color['ENDC'] + str(chain))
                print(color['LRED'] + "0." + color['ENDC'] + "Back")
                print()
                c = int(input(color['LGREEN'] + ">" + color['ENDC']))
                if c == 0:
                    continue
                else:
                    try:
                        select(c)
                    except IndexError:
                        print(color['LRED'] + 'Chain Not Found, Select A Valid Chain' + color['ENDC'])
                        pass
            elif choice == 2:
                os.system('clear')
                print(color['BLUE'] + "[PyBlock:NewChain]" + color['ENDC'])
                print()
                print(color['LGREEN'] + "1." + color['ENDC'] + "New")
                print(color['LGREEN'] + "2." + color['ENDC'] + "Copy From Previous Chain")
                print(color['LRED'] + "0." + color['ENDC'] + "Exit")
                print()
                c = int(input(color['LGREEN'] + ">" + color['ENDC']))
                if c == 0:
                    continue
                if c == 1:
                   name = input("Chain Name" + color['LGREEN'] + ">" + color['ENDC'])
                   chains.append(Chain(name))
                   print(color['GREEN'] + "New Chain Added" + color['ENDC'])
                   save()
                if c == 2:
                    idx = int(input("Chain Index" + color['LGREEN'] + ">" + color['ENDC']))
                    name = input("Chain Name" + color['LGREEN'] + ">" + color['ENDC'])
                    try:
                        c = chains[idx - 1].fork()
                        c.name = name
                        chains.append(c)
                        print(color['GREEN'] + "New Chain Added" + color['ENDC'])
                        save()
                    except IndexError:
                        print(color['LRED'] + 'Chain Not Found, Select A Valid Chain' + color['ENDC'])
                        pass

            else:
                print('\n' + color['LRED'] + "Keyboard Interrupt, Aborting Commit." + color['ENDC'])

    except KeyboardInterrupt:
        print('\n' + color['LRED'] + "Keyboard Interrupt, Aborting Commit." + color['ENDC'])


