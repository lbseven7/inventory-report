from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport
# from inventory_report.reports.complete_report import CompleteReport


# # 9 - Testar a geração de uma versão do relatório em cores

def test_decorar_relatorio():
    report = ColoredReport(SimpleReport)
    products_list = [
        {
            "nome_da_empresa": "Farinini",
            "nome_do_produto": "Farinha de Trigo",
            "data_de_fabricacao": "2022-04-04",
            "data_de_validade": "2023-02-09",
        },
        {

            "nome_da_empresa": "Farinini",
            "nome_do_produto": "Sabão em pó",
            "data_de_fabricacao": "2022-04-04",
            "data_de_validade": "2023-02-09",
        },
    ]

    res = report.generate(products_list)
    data_antiga = "Data de fabricação mais antiga:"
    data_validade = "Data de validade mais próxima:"
    empresa = "Empresa com mais produtos:"
    data_a = "2022-04-04"
    data_v = "2023-02-09"
    emp = "Farinini"

    assert f"\033[32m{data_antiga}\033[0m \033[36m{data_a}\033[0m" in res
    assert f"\033[32m{data_validade}\033[0m \033[36m{data_v}\033[0m" in res
    assert f"\033[32m{empresa}\033[0m \033[31m{emp}\033[0m" in res

# não consigo quebras as linhas sem "quebrar" o código no github!

# data_antiga = """\033[32m'Data de fabricação mais antiga:'
#     \033[0m \033[36m2022-04-04\033[0m\n"""

#     validade = """\033[32m'Data de validade mais próxima:'
#     \033[0m \033[36m2023-02-09\033[0m\n"""

#     empresa = """\033[32m'Empresa com mais produtos:'
#     \033[0m \033[31mFarinini\033[0m\n"""

#     result = report.generate(products_list)

#     assert data_antiga in result
#     assert validade in result
#     assert empresa in result

    # data_antiga = """\033[32m'Data de fabricação mais antiga:'
    #     "\033[0m 033[36m'1940-10-23'\033[0m\n"""
    # validade = """\033[32m'Data de validade mais próxima:'
    #     "\033[0m \033[36m2023-02-09\033[0m"""
    # empresa = """\033[32m'Empresa com mais produtos:'
    #     "\033[0m \033[31mFarinini\033[0m"""

    # return (
    #     f"Data de fabricação mais antiga: {data_antiga}\n"
    #     f"Data de validade mais próxima: {validade}\n"
    #     f"Empresa com mais produtos: {empresa}"
    # ) in result
