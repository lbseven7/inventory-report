import sys
import os
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


def main():
    # Verifica se o número de argumentos está correto
    if len(sys.argv) < 3:
        sys.stderr.write("Verifique os argumentos\n")
        return
    file_path = sys.argv[1]
    report_type = sys.argv[2]

    # desafio: diminuir a complexidade deste trecho
    importers = {
        '.csv': CsvImporter,
        '.json': JsonImporter,
        '.xml': XmlImporter
        }

    extension = os.path.splitext(file_path)[1]
    importer = importers.get(extension)
    if importer:
        inventory = InventoryRefactor(importer)

    data = inventory.import_data(file_path, report_type)

    if report_type == 'simples':
        return sys.stdout.write(SimpleReport.generate(data))
    elif report_type == 'completo':
        return sys.stdout.write(CompleteReport.generate(data))


if __name__ == '__main__':
    main()
