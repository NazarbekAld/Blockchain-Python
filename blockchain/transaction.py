
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
    def getTransaction(self, returns="hashmap") -> HashMap or dict:
        if returns == "hashmap":
            map = HashMap()
            map.put("payer", self.__payer)
            map.put("payee", self.__payee)
            map.put("amount", self.__amount)
            map.put("signature", self.__signature)
            return map
        elif returns == "dict":
            return {
                "Payer": self.__payer.getAddress().export_key().decode(),
                "Payee": self.__payee.getAddress().export_key().decode(),
                "Amount": self.__amount,
                "Signature": self.__signature.get().hexdigest()
                }