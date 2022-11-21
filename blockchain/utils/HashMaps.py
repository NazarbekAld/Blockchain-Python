# HASHMAP. No limits. Keys and values can be everything.
class HashMap():
    def __init__(self, debug=False, keys=[], values=[]) -> None:
        """
        Constructor
        """
        self.debug = debug
        self.__keys = []
        self.__values = values
        if keys != []:
            for i in keys:
                self.__keys.append(i.__hash__)
        
    def get(self, key, getCache=False) -> any:
        """
        Getting value from hashmap
        """
        if (self.debug):
            print(self, ":\nGetting value from: ", key, "...", sep="")
        index = 0
        hash = key.__hash__
        for a in range(len(self.__keys)):
            if self.__keys[a] == hash:
                if not getCache:
                    return self.__values[index]
                return HashMapElementCache(key, self.__values[index])
            index += 1
        return None
    def pop(self, key) -> None:
        """
        Deleting value.
        """
        if (self.debug):
            print(self, ":\nDeleting value from: ", key, "...", sep="")
        index = 0
        hash = key.__hash__
        for a in range(len(self.__keys)):
            try:
                if self.__keys[a] == hash:
                    self.__keys.pop(index)
                    self.__values.pop(index)
            except Exception as e:
                pass
            index += 1
        return None
    def put(self, key : str, value) -> None:
        if (self.debug):
            print(self, ":\nAdding key: ", key, ", value: ", value, "...", sep="")
        """
        Appends value to hashmap.
        """
        self.__keys.append(key.__hash__)
        self.__values.append(value)
    def getAll(self) -> list[any, any]:
        if (self.debug):
            print(self, ":\nGetting every value...", sep="")
        """
        Get keys, values.
        """
        return [self.__keys, self.__values]
    def getOf(self, value="values"):
        if (self.debug):
            print(self, ":\nGetting every of " + value)
        """
        Get private values.
        """
        if value == "keys":
            return self.__keys
        elif value == "values":
            return self.__values


# For most used results
class HashMapElementCache():
    def __init__(self, key, value) -> None:
        """
        Constructor
        """
        self.__key = key.__hash__
        self.__value = value
    def dropAll(self) -> list:
        """
        Get all.
        """
        return [self.__key, self.__value]
    def getValue(self) -> any:
        """
        Get value from cache.
        """
        return self.__value
    def getKey(self) -> any:
        """
        Get key from cache.
        """
        return self.__key