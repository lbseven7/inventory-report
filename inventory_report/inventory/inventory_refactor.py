# 10 - Criar uma classe InventoryIterator
from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.importer.csv_importer import CsvImporter


class InventoryRefactor():

    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def import_data(self, path, type):
        self.data.extend(self.importer.import_data(path))
        return self.data

    def __iter__(self):
        return InventoryIterator(self.data)

    def __next__(self):
        return self.data


if __name__ == '__main__':
    inventory = InventoryRefactor(CsvImporter)
    file_csv = inventory.import_data(
        'inventory_report/data/inventory.csv', 'simples')
    iterator = iter(inventory)
    first = next(iterator)
    second = next(iterator)
    print(first)
    print(second)
