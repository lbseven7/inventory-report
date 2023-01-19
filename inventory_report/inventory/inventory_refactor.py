# 10.1 - Seclass Inventory():
from inventory_iterator import InventoryIterator


class InventoryRefactor():
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def import_data(self, file_name):
        self.data += self.importer.import_data(file_name)

    def __iter__(self):
        return InventoryIterator(self.data)
