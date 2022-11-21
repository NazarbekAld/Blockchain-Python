
# Address

from Crypto.PublicKey.RSA import RsaKey
from Crypto.PublicKey import RSA

class Address():
    def __init__(self, address=RSA.generate(1028).public_key()) -> None:
        self.__address = address
    def getAddress(self) -> RsaKey:
        return self.__address
    def getAddressINstr(self) -> str:
        return self.__address.export_key()