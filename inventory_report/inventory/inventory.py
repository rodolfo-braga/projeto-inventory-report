import csv
import json
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    report = {'simples': SimpleReport, 'completo': CompleteReport}

    @classmethod
    def import_data(cls, path, type):
        with open(path, mode="r", encoding="utf-8") as file:
            if path.endswith(".csv"):
                data = csv.DictReader(file, delimiter=",", quotechar='"')
                list = [row for row in data]
                return cls.report[type].generate(list)

            elif path.endswith(".json"):
                list = json.load(file)
                return cls.report[type].generate(list)
