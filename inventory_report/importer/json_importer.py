from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if path.endswith(".json"):
            with open(path, mode="r", encoding="utf-8") as file:
                return json.load(file)
        else:
            raise ValueError("Arquivo inválido.")
