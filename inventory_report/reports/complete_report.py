from inventory_report.reports.simple_report import SimpleReport
from collections import Counter

# Gerar a versão completa do relatório


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, list):
        result = super().generate(list)
        result += '\nProdutos estocados por empresa:\n'

        list_nomes_empresas = []
        for item in list:
            list_nomes_empresas.append(item['nome_da_empresa'])

        estoque = Counter(list_nomes_empresas).most_common()
        for produto in estoque:
            result += f'- {produto[0]}: {produto[1]}\n'

        return result
