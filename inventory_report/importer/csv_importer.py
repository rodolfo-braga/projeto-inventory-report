from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if path.endswith(".csv"):
            with open(path, mode="r", encoding="utf-8") as file:
                data = csv.DictReader(file, delimiter=",", quotechar='"')
                return [row for row in data]
        else:
            raise ValueError("Arquivo inválido.")
