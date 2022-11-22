import json

import transaction
from Crypto.Hash import SHA256

# Block

class Block():
    def __init__(self, transactions : list[transaction.Transaction], lastblockhash=SHA256.new().hexdigest(), lastblockindex=0) -> None:
        self.__transactions = transactions
        self.__myhash = SHA256.new(data=lastblockhash.encode())
        self.__index = lastblockindex
    def getValues(self) -> list:
        return self.__transactions, self.__myhash
    def toJSON(self) -> str:
        a = {}
        for i in self.__transactions:
            a.append(json.dumps(i.getTransaction(returns="dict")))
        json.dumps({
            "index": self.__index,
            "Transactions" : a,
            "hash": self.__myhash
            })