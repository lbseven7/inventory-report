from inventory_report.inventory.product import Product


# 1 - Testar o construtor/inicializador do objeto Produto
# 1 - Deve criar um novo produto com todos os atributos
# corretamente preenchidos.

def test_cria_produto():
    product = Product(
        id=1,
        nome_do_produto="Café",
        nome_da_empresa="Nescafé",
        data_de_fabricacao="01/01/2021",
        data_de_validade="01/01/2022",
        numero_de_serie="123456789",
        instrucoes_de_armazenamento="em local seco",
        )

    assert product.id == 1
    assert product.nome_do_produto == "Café"
    assert product.nome_da_empresa == "Nescafé"
    assert product.data_de_fabricacao == "01/01/2021"
    assert product.data_de_validade == "01/01/2022"
    assert product.numero_de_serie == "123456789"
    assert product.instrucoes_de_armazenamento == "em local seco"
