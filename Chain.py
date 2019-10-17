import datetime, copy
from Block import Block

class Chain:
    def __init__(self,name):
        self.name = name
        self.blocks = [self.genesis()]

    def __str__(self):
        return self.name

    def genesis(self):
        return Block(0, str(datetime.datetime.utcnow()), "mint", "genesis")

    def add(self, data):
        self.blocks.append(Block(len(self.blocks), str(datetime.datetime.utcnow()), data, self.blocks[-1].hash))

    def manualadd(self, data):
        self.blocks.append(Block(len(self.blocks), str(datetime.datetime.utcnow()), data, self.blocks[-1].hash))

    def length(self):
        return len(self.blocks)

    def verify(self, verbose=True):
        flag = True
        for index, block in enumerate(self.blocks):
            if index == 0:
                if verbose:
                    print("Genesis Block, Skipping")
            else:
                if block.index != index:
                    flag = False
                    if verbose:
                        print("Mismatched Index at ", index)
                elif block.previous_hash != self.blocks[index - 1].hash:
                    flag = False
                    if verbose:
                        print("Mismatched Previous Block Hash at ", index)
                elif block.hash != block.hash():
                    flag = False
                    if verbose:
                        print("Mismatched Hash at ", index)
                elif block.timestamp <= self.blocks[index - 1].timestamp:
                    flag = False
                    if verbose:
                        print("Backdating at ", index)
            return flag

    def fork(self, head="latest"):
        if head in ['latest', 'all', 'whole']:
            return copy.deepcopy(self)
        else:
            newblock = copy.deepcopy(self)
            newblock.blocks = self.blocks[0:head+1]
            return newblock


