from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    @staticmethod
    def import_data(file_name: str):
        if not file_name.endswith('.xml'):
            raise ValueError('Arquivo inválido')
        data = []
        tree = ET.parse(file_name)
        root = tree.getroot()
        for item in root.findall('item'):
            item_data = {}
            for child in item:
                item_data[child.tag] = child.text
            data.append(item_data)
        return data

    # Ajuda do https://chat.openai.com/chat
