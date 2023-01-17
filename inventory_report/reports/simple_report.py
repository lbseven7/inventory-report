from collections import Counter

# 2 - Gerar a versão simplificada do relatório
# O relatório deve ser gerado através de um método
# estático ou de classe chamado generate escrito dentro da classe SimpleReport.


class SimpleReport:
    @staticmethod
    def generate(list):
        data_list_fabricacao = []
        for item in list:
            data_list_fabricacao.append(item['data_de_fabricacao'])

        data_list_validade = []
        for item in list:
            data_list_validade.append(item['data_de_validade'])

        list_nomes_empresas = []
        for item in list:
            list_nomes_empresas.append(item['nome_da_empresa'])

        nome_da_empresa_com_mais_produtos = Counter(
            list_nomes_empresas).most_common()[0][0]

        print(nome_da_empresa_com_mais_produtos)

        return (
            f'Data de fabricação mais antiga: {min(data_list_fabricacao)}\n'
            f'Data de validade mais próxima: {min(data_list_validade)}\n'
            f'Empresa com mais produtos: {nome_da_empresa_com_mais_produtos}'
        )
