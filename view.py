import controller
import os.path

def criaArquivos(*nome):
    for i in nome:
        if not os.path.exists(i):
            with open(i, 'w') as arq:
                arq.writelines('')
criaArquivos("categoria.txt",
             "clientes.txt",
             "estoque.txt",
             "fornecedores.txt",
             "funcionarios.txt",
             "venda.txt")

if __name__ == "__main__":
    while True:
        menu_principal = int(input("""
        1 - CATEGORIAS
        2 - ESTOQUE
        3 - FORNECEDORES
        4 - CLIENTES
        5 - FUNCIONARIOS
        6 - VENDAS
        7 - SAIR
        DIGITE UM NÚMERO: """))
        
        if menu_principal == 1:
            categoria = controller.ControllerCategoria()
            while True:
                opcoes_categoria = int(input(""" 
                1 - CADASTRAR CATEGORIA
                2 - REMOVER CATEGORIA
                3 - ALTERAR CATEGORIA
                4 - MOSTRAR CATEGORIAS
                5 - SAIR
                DIGITE UM NÚMERO: """))
                if opcoes_categoria == 1:
                    cadastra_categoria = input('Categoria: ')
                    categoria.cadastraCategoria(cadastra_categoria)
                elif opcoes_categoria == 2:
                    remover_categoria = input('Remover categoria: ')
                    categoria.removerCategoria(remover_categoria)
                elif opcoes_categoria == 3:
                    alterar_cateforia = input('Alterar categoria: ')
                    categoria_alterada = input('Nova categoria: ')
                    categoria.alterarCategoria(alterar_cateforia, categoria_alterada)
                elif opcoes_categoria == 4:
                    categoria.mostrarCategoria()
                else:
                    break

        elif menu_principal == 2:
            estoque = controller.ControllerEstoque()
            while True:
                opcoes_estoque = int(input(""" 
                1 - CADASTRAR PRODUTO
                2 - REMOVER PRODUTO
                3 - MOSTRAR ESTOQUE
                4 - SAIR
                DIGITE UM NÚMERO: """))

                if opcoes_estoque == 1:
                    nome_produto = input('Nome do produto: ')
                    preco_produto = input('Preço: ')
                    categoria_produto = input('Categoria: ')
                    quantidade_produto = input('Quantidade: ')
                    estoque.cadastrarProduto(nome_produto, preco_produto, categoria_produto, quantidade_produto)
                elif opcoes_estoque == 2:
                    remove_produto = input('Remover produto: ')
                    estoque.removerProduto(remove_produto)
                elif opcoes_estoque == 3:
                    estoque.mostrarEstoque()
                else:
                    break

        elif menu_principal == 3:
            fornecedores = controller.ControllerFornecedor()
            while True:
                opcoes_fornecedores = int(input(""" 
                1 - CADASTRAR FORNECEDOR
                2 - ALTERAR FORNECEDOR
                3 - REMOVER FORNECEDOR
                4 - MOSTRAR FORNECEDORES
                5 - SAIR
                DIGITE UM NÚMERO: """))
                if opcoes_fornecedores == 1:
                    nome_fornecedor = input('Nome: ')
                    cnpj_fornecedor = input('CNPJ: ')
                    teleforne_fornecedor = input('Telefone: ')
                    categoria_fornecedor = input('Categoria: ')
                    fornecedores.cadastraFornecedor(nome_fornecedor, cnpj_fornecedor, teleforne_fornecedor, categoria_fornecedor)
                elif opcoes_fornecedores == 2:
                    nome_fornecedor_alterar = input('Fornecedor: ')
                    novo_nome_fornecedor = input('Novo nome: ')
                    novo_cnpj_fornecedor = input('Novo CNPJ: ')
                    novo_telefone_fornecedor = input('Novo telefone: ')
                    nova_categoria_fornecedor = input('Nova categoria: ')
                    fornecedores.alterarFornecedor(nome_fornecedor_alterar, novo_nome_fornecedor, novo_cnpj_fornecedor, novo_telefone_fornecedor, nova_categoria_fornecedor)
                elif opcoes_fornecedores == 3:
                    remover_fornecedor = input('Fornecedor: ')
                    fornecedores.removerFornecedor(remover_fornecedor)
                elif opcoes_fornecedores == 4:
                    fornecedores.mostrarFornecedores()
                else:
                    break

        elif menu_principal == 4:
            clientes = controller.ControllerClientes()
            while True:
                opcoes_clientes = int(input(""" 
                1 - CADASTRAR CLIENTE
                2 - ALTERAR CLIENTE
                3 - REMOVER CLIENTE
                4 - MOSTRAR CLIENTES
                5 - SAIR
                DIGITE UM NÚMERO: """))
                if opcoes_clientes == 1:
                    nome_cliente = input('Nome: ')
                    telefone_cliente = input('Telefone: ')
                    cpf_cliente = input('CPF: ')
                    email_cliente = input('E-mail: ')
                    endereco_cliente = input('Endereço: ')
                    clientes.cadastrarCliente(nome_cliente, telefone_cliente, cpf_cliente, email_cliente, endereco_cliente)
                elif opcoes_clientes == 2:
                    nome_cliente_alterar = input('Cliente: ')
                    novo_nome_cliente = input('Novo nome: ')
                    novo_telefone_cliente = input('Novo telefone: ')
                    novo_cpf_cliente = input('Novo CPF: ')
                    novo_email_cliente = input('Novo e-mail: ')
                    novo_endereco_cliente = input('Novo endereço: ')
                    clientes.alterarCliente(nome_cliente_alterar, novo_nome_cliente, novo_telefone_cliente, novo_cpf_cliente, novo_email_cliente, novo_endereco_cliente)
                elif opcoes_clientes == 3:
                    remover_cliente = input('Cliente: ')
                    clientes.removerCliente(remover_cliente)
                elif opcoes_clientes == 4:
                    clientes.mostrarClientes()
                else:
                    break

        elif menu_principal == 5:
            funcionario = controller.ControllerFuncionario()
            while True:
                opcoes_funcionario = int(input(""" 
                1 - CADASTRAR FUNCIONÁRIO
                2 - ALTERAR FUNCIONARIO
                3 - REMOVER FUNCIONARIO
                4 - MOSTRAR FUNCIONARIOS
                5 - SAIR
                DIGITE UM NÚMERO: """))
                if opcoes_funcionario == 1:
                    clt_funcionario = input('CLT: ')
                    nome_funcionario = input('Nome: ')
                    telefone_funcionario = input('Telefone: ')
                    cpf_funcionario = input('CPF: ')
                    email_funcionario = input('E-mail: ')
                    endereco_funcionario = input('Endereço: ')
                    funcionario.cadastrarFuncionario(clt_funcionario, nome_funcionario, telefone_funcionario, cpf_funcionario, email_funcionario, endereco_funcionario)
                elif opcoes_funcionario == 2:
                    nome_funcionario_alterar = input('Funcionario: ')
                    nova_clt_funcionario = input('Nova CLT: ')
                    novo_nome_funcionario = input('Novo Nome: ')
                    novo_telefone_funcionario = input('Novo telefone: ')
                    novo_cpf_funcionario = input('Novo CPF: ')
                    novo_email_funcionario = input('Novo e-mail: ')
                    novo_endereco_funcionario = input('Novo Endereço: ')
                    funcionario.alterarFuncionario(nome_funcionario_alterar, nova_clt_funcionario, novo_nome_funcionario, novo_telefone_funcionario, novo_cpf_funcionario, novo_email_funcionario, novo_endereco_funcionario)
                elif opcoes_funcionario == 3:
                    remover_funcionario = input('Funcionario: ')
                    funcionario.removerFuncionario(remover_funcionario)
                elif opcoes_funcionario == 4:
                    funcionario.mostrarFuncionarios()
                else:
                    break

        elif menu_principal == 6:
            vendas = controller.ControllerVenda()
            while True:
                opcoes_venda = int(input(""" 
                1 - CADASTRAR VENDA
                2 - RELATORIO TOTAL DE VENDAS
                3 - FILTRO DE VENDAS
                4 - SAIR
                DIGITE UM NÚMERO: """))
                if opcoes_venda == 1:
                    nome_produto = input('Produto: ')
                    nome_vendedor = input('Vendedor: ')
                    nome_comprador = input('Cliente: ')
                    quantidade_venda = input('Quantidade: ')
                    vendas.cadastrarVenda(nome_produto, nome_vendedor, nome_comprador, quantidade_venda)
                elif opcoes_venda == 2:
                    vendas.relatorioVendasTotal()
                elif opcoes_venda == 3:
                    data_inicio = input('Data inicial: ')
                    data_final = input('Data final: ')
                    vendas.filtroVendas(data_inicio, data_final)
                else:
                    break

        else:
            break
