
import transaction
from Crypto.Hash import SHA256

# Block

class Block():
    def __init__(self, transactions : list[transaction.Transaction], lastblockhash=SHA256.new()) -> None:
        pass