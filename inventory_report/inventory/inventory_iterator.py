# Criar uma classe InventoryIterator

class InventoryIterator():
    def __init__(self, products):
        self.__products = products
        self.__index = 0

    def __next__(self):
        if self.__index < len(self.__products):
            product = self.__products[self.__index]
            self.__index += 1
            return product
        raise StopIteration

    def __iter__(self):
        return self

# Consulta em: https://www.geeksforgeeks.org/iterators-in-python/
