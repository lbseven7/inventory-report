from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @staticmethod
    def import_data(path):
        if path.endswith('.csv'):
            with open(path, 'r') as arquivo_csv:
                return list(csv.DictReader(arquivo_csv))
        raise ValueError('Arquivo inválido')
