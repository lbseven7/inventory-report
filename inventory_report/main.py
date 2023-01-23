import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor


def main():

    if len(sys.argv) < 3:
        sys.stderr.write("Verifique os argumentos")
        sys.exit(1)

    file_path = sys.argv[1]
    report_type = sys.argv[2]

    inventory = InventoryRefactor(file_path)
    report = inventory.generate_report(report_type)
    return report


if __name__ == '__main__':
    main()
