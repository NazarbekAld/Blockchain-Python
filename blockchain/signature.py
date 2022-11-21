
from Crypto.PublicKey import RSA
from Crypto.Hash.SHA256 import SHA256Hash

# Signature from node

class Signature():
    def __init__(self, signature : SHA256Hash) -> None:
        self.__signature = signature
    def get(self) -> SHA256Hash:
        return self.__signature
    def getstring(self) -> str:
        return self.__signature.hexdigest()