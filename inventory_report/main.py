import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.importer.importer import Importer


def main():
    # Verifica se o número de argumentos está correto
    if len(sys.argv) < 3:
        sys.stderr.write("Verifique os argumentos")
    return


inventory = InventoryRefactor(Importer)

file_path = sys.argv[1]
report_type = sys.argv[2]

if report_type == 'csv':
    inventory.import_data(CsvImporter)
elif report_type == "json":
    inventory.import_data(JsonImporter)
elif report_type == "xml":
    inventory.import_data(XmlImporter)
else:
    sys.stdout.write("Verifique os argumentos")

print(inventory.import_data(file_path, report_type))
