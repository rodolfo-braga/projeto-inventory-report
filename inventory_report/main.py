import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def main():
    if len(sys.argv) != 3:
        sys.stderr.write("Verifique os argumentos\n")
        return

    args_list = sys.argv
    file_path = args_list[1]
    report_type = args_list[2]

    file_extension = file_path.split(".")[-1]
    if file_extension not in ["csv", "json", "xml"]:
        sys.stderr.write("Arquivo inválido\n")
        return

    importer = {"csv": CsvImporter, "json": JsonImporter, "xml": XmlImporter}
    inventory = InventoryRefactor(importer[file_extension])
    report = inventory.import_data(file_path, report_type)
    sys.stdout.write(report)
