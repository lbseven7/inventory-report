# 4 - Gere os relatórios através de um arquivo CSV
# import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xmltodict


class Inventory():

    @staticmethod
    def import_data(path, type):
        if type == 'simples':
            return SimpleReport.generate(Inventory.ler_arquivo(path))
        elif type == 'completo':
            return CompleteReport.generate(Inventory.ler_arquivo(path))

    @staticmethod
    def ler_arquivo(path):
        if path.endswith('.csv'):
            with open(path, 'r') as arquivo_csv:
                return list(csv.DictReader(arquivo_csv))

        elif path.endswith('.json'):
            with open(path, 'r') as arquivo_json:
                return json.load(arquivo_json)

        elif path.endswith('.xml'):
            with open(path, 'r') as arquivo_xml:
                return xmltodict.parse(arquivo_xml.read())['dataset']['record']

# Ajuda de Arlisson