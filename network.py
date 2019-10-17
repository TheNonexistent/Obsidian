from socket import *
import json
def listen():
    chains_socket=socket(AF_INET, SOCK_DGRAM)
    chains_socket.bind(('',2446))
while True:
    chains_data=chains_socket.recvfrom(1024)
    try:
        new_chains = json.loads(chain_data)
        for new_chain in new_chains:
            chain = Chain(new_chain['name'])
            for i, block in enumerate(new_chain['blocks']):
                chain.blocks[i].__dict__ = block
            chains.append(ne)
    except:
        pass

def broadcast():