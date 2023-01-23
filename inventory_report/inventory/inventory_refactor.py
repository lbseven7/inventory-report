# 10 - Criar uma classe InventoryIterator
from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor():

    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def import_data(self, path, type):
        self.data = self.importer.import_data(path)
        return self.data

    def __iter__(self):
        return InventoryIterator(self.data)

    def __next__(self):
        return next(self.importer)
