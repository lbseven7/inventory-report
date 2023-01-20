# 10 - Criar uma classe InventoryIterator
from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor():
    def __init__(self, products):
        self.__products = products

    def __iter__(self):
        return InventoryIterator(self.__products)

    def __next__(self):
        return next(self.__products)
