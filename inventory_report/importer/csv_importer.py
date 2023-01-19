from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @staticmethod
    def import_data(file_name: str):
        if not file_name.endswith('.csv'):
            raise ValueError('Arquivo inválido')
        data = []
        with open(file_name, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
        return data

# Ajuda do https://chat.openai.com/chat
