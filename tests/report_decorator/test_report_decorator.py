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
    result = report.generate(products_list)
    assert "\033[32mData de fabricação mais antiga:\033[0m \033[36m2022-04-04\033[0m" in result
    assert "\033[32mData de validade mais próxima:\033[0m \033[36m2023-02-09\033[0m" in result
    assert "\033[32mEmpresa com mais produtos:\033[0m \033[31mFarinini\033[0m" in result
