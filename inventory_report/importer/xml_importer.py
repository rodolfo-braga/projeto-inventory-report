from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if path.endswith(".xml"):
            with open(path, mode="r", encoding="utf-8") as file:
                data = xmltodict.parse(file.read())
                return data["dataset"]["record"]
        else:
            raise ValueError("Arquivo inválido.")
