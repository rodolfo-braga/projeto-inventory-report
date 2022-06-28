from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def get_companies_stock(list):
        items_by_company = {}
        for item in list:
            print(item)
            if item["nome_da_empresa"] not in items_by_company:
                items_by_company[item["nome_da_empresa"]] = 1
            else:
                items_by_company[item["nome_da_empresa"]] += 1

        return items_by_company.items()

    def generate_report_complement(cls, list):
        report_complement = ''
        companies_stock = cls.get_companies_stock(list)
        for company, stock in companies_stock:
            report_complement += f"- {company}: {stock}\n"

        return report_complement

    @classmethod
    def generate(cls, list):
        simple_report = super().generate(list)
        report_complement = cls.generate_report_complement(cls, list)
        return (
            f"{simple_report}\n"
            "Produtos estocados por empresa:\n"
            f"{report_complement}"
        )
