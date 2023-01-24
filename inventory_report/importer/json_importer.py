import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @staticmethod
    def import_data(path):
        if path.endswith('.json'):
            with open(path, 'r') as arquivo_json:
                return json.load(arquivo_json)
        else:
            raise ValueError('Arquivo inválido')
