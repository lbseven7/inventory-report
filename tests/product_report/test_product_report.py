from inventory_report.inventory.product import Product


# 8 - Testar o relatório individual do produt0
def test_relatorio_produto():
    product = Product(
        id=1,
        nome_do_produto="Café",
        nome_da_empresa="Nescafe",
        data_de_fabricacao="01/01/2021",
        data_de_validade="01/01/2022",
        numero_de_serie="123456789",
        instrucoes_de_armazenamento="em local seco",
    )

    str_product = str(product)
    assert (str_product) == (
        f"O produto {product.nome_do_produto}"
        f" fabricado em {product.data_de_fabricacao}"
        f" por {product.nome_da_empresa} com validade"
        f" até {product.data_de_validade}"
        f" precisa ser armazenado {product.instrucoes_de_armazenamento}."
    )
