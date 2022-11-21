
import address
from signature import Signature
from Crypto.Hash import SHA256

from utils.HashMaps import HashMap

# import pickle

# Transactions.

class Transaction():

    def __init__(self, payer : address.Address, payee : address.Address, amount : float, signature : Signature) -> None:
        self.__payer = payer
        self.__payee = payee
        self.__amount = amount
        self.__signature = signature
    def getTransaction(self) -> HashMap:
        map = HashMap()
        map.put("payer", self.__payer)
        map.put("payee", self.__payee)
        map.put("amount", self.__amount)
        map.put("signature", self.__signature)
        return map
