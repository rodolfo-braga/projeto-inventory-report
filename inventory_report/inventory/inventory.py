import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, path, report_type):
        with open(path, mode="r", encoding="utf-8") as file:
            data = csv.DictReader(file, delimiter=",", quotechar='"')
            list = [row for row in data]

            if report_type == 'simples':
                return SimpleReport.generate(list)

            if report_type == 'completo':
                return CompleteReport.generate(list)
