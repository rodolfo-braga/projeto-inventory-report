from datetime import date


class SimpleReport:
    def get_oldest_manufacturing_date(list):
        datas_de_fabricacao = [
            item["data_de_fabricacao"] for item in list
        ]
        return min(datas_de_fabricacao)

    def get_closest_expiration_date(list):
        datas_de_validade = [
            item["data_de_validade"] for item in list
            if item["data_de_validade"] >= str(date.today())
        ]
        return min(datas_de_validade)

    def get_company_bigger_stock(list):
        items_by_company = {}
        for item in list:
            if item["nome_da_empresa"] not in items_by_company:
                items_by_company[item["nome_da_empresa"]] = 1
            else:
                items_by_company[item["nome_da_empresa"]] += 1
        return max(items_by_company, key=items_by_company.get)

    @classmethod
    def generate(cls, list):
        oldest_manufacturing_date = cls.get_oldest_manufacturing_date(list)
        closest_expiration_date = cls.get_closest_expiration_date(list)
        company_bigger_stock = cls.get_company_bigger_stock(list)
        return (
            f"Data de fabricação mais antiga: {oldest_manufacturing_date}\n"
            f"Data de validade mais próxima: {closest_expiration_date}\n"
            f"Empresa com mais produtos: {company_bigger_stock}"
        )
