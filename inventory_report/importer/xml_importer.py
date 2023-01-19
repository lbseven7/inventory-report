import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        if path.endswith('.xml'):
            with open(path, 'r') as arquivo_xml:
                return xmltodict.parse(arquivo_xml.read())['dataset']['record']
        raise ValueError('Arquivo inválido')
