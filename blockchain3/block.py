from collections import OrderedDict
from dataclasses import dataclass

@dataclass
class Tansactions:
    
        sender: str
        empfaenger: str
        geldmenge = int



@dataclass
class Block:
    
    last_hash: str
    transaction:OrderedDict
    nonce:int
    actual_hash: str


@dataclass
class Blockchain:

    blockchain: list
