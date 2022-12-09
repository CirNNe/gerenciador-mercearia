from models import *
from DAO import *
from datetime import datetime

class ControllerCategoria:
    def cadastraCategoria(self, novaCategoria):
        existe = False
        lista_categorias = DaoCategoria.ler() # JOGA A LISTA DE CATEGORIAS DENTRO DA VARIÁVEL
        for i in lista_categorias:
            if i.categoria == novaCategoria: # SE NA LISTA DE CATEGORIAS EXISTIR UMA IGUAL A QUE ESTAMOS CADASTRANDO, RETORNA TRUE
                existe = True
        if not existe:
            DaoCategoria.salvar(novaCategoria) # SE NÃO EXISTE, SALVA A CATEGORIA QUE ESTAMOS CADASTRANDO
            print('Categoria cadastrada!')
        else:
            print('Categoria já existe!')

    def removerCategoria(self, categoriaRemover):
        lista_categorias = DaoCategoria.ler()
        filtra_categorias = list(filter(lambda x: x.categoria == categoriaRemover, lista_categorias)) # FILTRA AS CATEGORIAS E RETORNA A CATEGORIA QUE DESEJAMOS REMOVER PARA A VARIAVEL
        if len(filtra_categorias) == 0: # SE, APÓS O FILTRO, A VARIAVEL ESTIVER VAZIA, ENTÃO NÃO EXISTE A CATEGORIA
            print('A categoria não existe!')
        else:
            for i in range(len(lista_categorias)): # SE A CATEGORIA QUE DESEJAMOS APAGAR ESTIVER NA LISTA, APAGA DA VARIÁVEL QUE CONTÉM A LISTA DAS CATEGORIAS
                if lista_categorias[i].categoria == categoriaRemover:
                    del lista_categorias[i]
                    break
            print('Categoria removida com sucesso!')
            with open('categoria.txt', 'w') as arq: # SOBRESCREVE O ARQUIVO COM AS CATEGORIAS DA VARIÁVEL QUE CONTÉM AS CATEGORIAS ATUALIZADAS SEM A QUE DESEJAMOS APAGAR
                for i in lista_categorias:
                    arq.writelines(i.categoria)
                    arq.writelines('\n')

        att_categoria_estoque = DaoEstoque.ler()
        att_categoria_estoque = list(map(lambda x: Estoque(Produtos(x.produto.nome, x.produto.preco, "Sem categoria"), x.quantidade) if(x.produto.categoria == categoriaRemover) else(x), att_categoria_estoque))
        # ATUALIZA A CATEGORIA DO PRODUTO NO ESTOQUE PARA: SEM CATEGORIA, CASO A CATEGORIA SEJA EXCLUIDA
        with open('estoque.txt', 'w') as arq:
            for i in att_categoria_estoque:
                arq.writelines(i.produto.nome + '|' + i.produto.preco + '|' + i.produto.categoria + '|' + str(i.quantidade))
                arq.writelines('\n')

    def alterarCategoria(self, categoriaAlterar, caltegoriaAlterada):
        lista_categorias = DaoCategoria.ler()
        filtra_categorias = list(filter(lambda x: x.categoria == categoriaAlterar, lista_categorias)) # FILTRA A CATEGORIA QUE DESEJAMOS ALTERAR
        if len(filtra_categorias) > 0:
            categoria_existe = list(filter(lambda x: x.categoria == caltegoriaAlterada, lista_categorias)) # CHECA SE EXISTE A CATEGORIA PARA A QUAL DESEJA ALTERAR NA LISTA DE CATEGORIAS
            if len(categoria_existe) == 0:
                lista_categorias = list(map(lambda x: Categoria(caltegoriaAlterada) if(x.categoria == categoriaAlterar) else(lista_categorias), lista_categorias))
                # ADICIONA NA LISTA DE CATEGORIAS A CATEGORIA ALTERADA SE ELA FOR IGUAL A CATEGORIA QUE DESEJAMOS ALTERAR, SENÃO, MANTEM A LISTA
                print('A categoria foi alterada com sucesso!')

                att_categoria_estoque = DaoEstoque.ler()
                att_categoria_estoque = list(map(lambda x: Estoque(Produtos(x.produto.nome, x.produto.preco, caltegoriaAlterada), x.quantidade) if(x.produto.categoria == categoriaAlterar) else(x), att_categoria_estoque))
                # ALTERA A CATEGORIA DO PRODUTO NO ESTOQUE CASO A CATEGORIA SEJA ALTERADA
                with open('estoque.txt', 'w') as arq:
                    for i in att_categoria_estoque:
                        arq.writelines(i.produto.nome + '|' + i.produto.preco + '|' + i.produto.categoria + '|' + str(i.quantidade))
                        arq.writelines('\n')

            else:
               print('A categoria para qual deseja alterar já existe!')
        else:
            print('A categoria que deseja alterar não existe!')
        with open('categoria.txt', 'w') as arq: # SOBRESCREVE O ARQUIVO COM AS CATEGORIAS ATUALIAZADAS, COM A ALTERAÇÃO
            for i in lista_categorias:
                arq.writelines(i.categoria)
                arq.writelines('\n')

    def mostrarCategoria(self):
        categorias = DaoCategoria.ler()
        if len(categorias) == 0:
            print('Lista de categorias vazia!')
        else:
            for i in categorias:
                print(f'Categoria: {i.categoria}')
    

class ControllerEstoque:
    def cadastrarProduto(self, nome, preco, categoria, quantidade):
        lista_estoque = DaoEstoque.ler()
        lista_categoria = DaoCategoria.ler()
        filtra_estoque = list(filter(lambda x: x.produto.nome == nome, lista_estoque)) # CHECA SE EXISTE O PRODUTO NO ESTOQUE
        filtra_categoria = list(filter(lambda x: x.categoria == categoria, lista_categoria)) # CHECA SE EXTISTE A CATEGORIA PASSADA COMO PARÂMETRO
        if len(filtra_categoria) > 0: # SE EXISTIR A CATEGORIA, SEGUE O PROGRAMA
            if len(filtra_estoque) == 0: # SE NÃO EXISTIR O PRODUTO NO ESTOQUE, SEGUE PARA O CADASTRO
                produto = Produtos(nome, preco, categoria)
                DaoEstoque.salvar(produto, quantidade) # CADASTRA O PRODUTO
                print('Produto cadastrado com sucesso!')
            else:
                print('Produto já existe em estoque!')
        else:
            print('Categoria não existe!')

    def removerProduto(self, nome):
        lista_estoque = DaoEstoque.ler()
        filtrar_estoque = list(filter(lambda x: x.produto.nome == nome, lista_estoque)) # FILTRA O NOME DO PRODUTO
        if len(filtrar_estoque) > 0:
            for i in range(len(lista_estoque)):
                if lista_estoque[i].produto.nome == nome:
                    del lista_estoque[i]
                    break
            print('Produto removido com sucesso!')
        else:
            print('O produto não existe!')
        with open('estoque.txt', 'w') as arq:
            for i in lista_estoque: # RESCREVE O ARQUIVO COM OS VALORES DA LISTA
                arq.writelines(i.produto.nome + '|' +
                                i.produto.preco + '|' +
                                i.produto.categoria + '|' +
                                str(i.quantidade))
                arq.writelines('\n')

    def mostrarEstoque(self):
        estoque = DaoEstoque.ler()
        if len(estoque) == 0:
            print('Estoque vazio')
        else:
            print('########## PRODUTOS ##########')
            for i in estoque:
                print(f'Nome: {i.produto.nome}')
                print(f'Preço: {i.produto.preco}')
                print(f'Categoria: {i.produto.categoria}')
                print(f'Quantidade: {i.quantidade}')
                print('--------------------')


class ControllerVenda:
    def cadastrarVenda(self, nomeProduto, vendedor, comprador, quantidadeVendida):
        lista_estoque = DaoEstoque.ler()
        lista_estoque_att = []
        existe_produto = False
        quantidade_suficiente = False
        for i in lista_estoque:
            if i.produto.nome == nomeProduto:
                existe_produto = True
                if str(i.quantidade) >= quantidadeVendida:
                    quantidade_suficiente = True
                    i.quantidade = int(i.quantidade) - int(quantidadeVendida)
                    vendido = Venda(Produtos(i.produto.nome, i.produto.preco, i.produto.categoria), vendedor, comprador, quantidadeVendida)
                    valor_compra = int(quantidadeVendida) * int(i.produto.preco)
                    DaoVenda.salvar(vendido)
        lista_estoque_att.append(Estoque(Produtos(i.produto.nome, i.produto.preco, i.produto.categoria), i.quantidade))
        arq = open('estoque.txt', 'w')
        arq.writelines('')
        for i in lista_estoque_att:
            with open('estoque.txt', 'a') as arq:
                arq.writelines(i.produto.nome + '|' + i.produto.preco + '|' + i.produto.categoria + '|' + str(i.quantidade))
                arq.writelines('\n')
        if existe_produto == False:
            print('O produto não existe!')
            return None
        elif not quantidade_suficiente:
            print(f'Quantidade insuficiente no estoque para venda!')
        else:
            print('Venda realizada com sucesso!')
            return valor_compra

    def relatorioVendasTotal(self):
        vendas = DaoVenda.ler()
        produtos = []
        for i in vendas:
            nome = i.itensVendidos.nome
            quantidade_vendida = i.quantidadeVendida
            filtra_produtos = list(filter(lambda x: x['produto'] == nome, produtos))
            if len(filtra_produtos) > 0:
                produtos = list(map(lambda x: {'produto': nome, 'quantidade': int(x['quantidade']) + int(quantidade_vendida)} 
                if (x['produto'] == nome) else(x), produtos))
            else:
                produtos.append({'produto': nome, 'quantidade': int(quantidade_vendida)})
        lista_produtos_ordenada = sorted(produtos, key=lambda k: k['quantidade'], reverse=True)
        if len(lista_produtos_ordenada) > 0:
            print(f'##### PRODUTOS #####\n')
            for i in lista_produtos_ordenada:
                print(f"Produto: {i['produto']}")
                print(f"Quantidade Vendida: {i['quantidade']}")
                print('-------------------------')
        else:
            print('Lista de vendas vazia!')

    def filtroVendas(self, dataInicio, dataFim):
        vendas = DaoVenda.ler()
        dataInicio = datetime.strptime(dataInicio, '%d/%m/%Y')
        dataFim = datetime.strptime(dataFim, '%d/%m/%Y')
        filtro_vendas = list(filter(lambda x: datetime.strptime(x.data, '%d/%m/%Y') >= dataInicio
                                    and datetime.strptime(x.data, '%d/%m/%Y') <= dataFim, vendas))
        valor_final = 0
        if len(vendas) > 0:
            print(f'##### RELATÓRIO DE VENDAS #####\n')
            for i in filtro_vendas:
                print(f'Nome: {i.itensVendidos.nome}')
                print(f'Categoria: {i.itensVendidos.categoria}')
                print(f'Data da Venda: {i.data}')
                print(f'Quantidade Vendida: {i.quantidadeVendida}')
                print(f'Comprador: {i.cliente}')
                print(f'Vendedor: {i.vendedor}')
                valor_final += int(i.itensVendidos.preco) * int(i.quantidadeVendida)
                print('------------------------------')
            print(f'Valor Total das Vendas: {valor_final}')
        else:
            print('Lista de vendas vazia!')


class ControllerFornecedor:
    def cadastraFornecedor(self, nome, cnpj, telefone, categoria):
        lista_fornecedor = DaoFornecedor.ler()
        filtra_cnpj = list(filter(lambda x: x.cnpj == cnpj, lista_fornecedor))
        filtra_telefone = list(filter(lambda x: x.telefone == telefone, lista_fornecedor))
        if len(filtra_cnpj) > 0:
            print('CNPJ já existe!')
        elif len(filtra_telefone) > 0:
            print('Telefone já existe!')
        else:
            if len(cnpj) == 14 and len(telefone) <= 11 and len(telefone) >= 10:
                DaoFornecedor.salvar(Fornecedor(nome, cnpj, telefone, categoria))
                print('Fornecedor cadastrado com sucesso!')
            else:
                print('Digite um cnpj ou telefone válido!')
        
    def alterarFornecedor(self, nomeAlterar, novoNome, novoCnpj, novoTelefone, novaCategoria):
        lista_fornecedor = DaoFornecedor.ler()
        filtra_fornecedor = list(filter(lambda x: x.nome == nomeAlterar, lista_fornecedor))
        if len(filtra_fornecedor) > 0:
            filtra_fornecedor = list(filter(lambda x: x.cnpj == novoCnpj, lista_fornecedor))
            if len(filtra_fornecedor) == 0:
                lista_fornecedor = list(map(lambda x: Fornecedor(novoNome, novoCnpj, novoTelefone, novaCategoria) if(x.nome == nomeAlterar) else(lista_fornecedor), lista_fornecedor))
            else:
                print('CNPJ já existe!')
        else:
            print('O fornecedor que deseja alterar não existe!')
        
        with open('fornecedores.txt', 'w') as arq:
            for i in lista_fornecedor:
                arq.writelines(i.nome + '|' + i.cnpj + '|' + i.telefone + '|' + str(i.categoria))
                arq.writelines('\n')
            print('Fornecedor alterado com sucesso!')
    
    def removerFornecedor(self, nome):
        lista_fornecedor = DaoFornecedor.ler()
        filtra_fornecedor = list(filter(lambda x: x.nome == nome, lista_fornecedor))
        if len(filtra_fornecedor) > 0:
            for i in range(len(lista_fornecedor)):
                if lista_fornecedor[i].nome == nome:
                    del lista_fornecedor[i]
                    break
        else:
            print('O fornecedor que deseja remover não existe!')
            return None
        with open('fornecedores.txt', 'w') as arq:
            for i in lista_fornecedor:
                arq.writelines(i.nome + '|' + i.cnpj + '|' + i.telefone + '|' + str(i.categoria))
                arq.writelines('\n')
            print('Fornecedor removido com sucesso!')
        
    def mostrarFornecedores(self):
        lista_fornecedor = DaoFornecedor.ler()
        if len(lista_fornecedor) == 0:
            print('A lista de fornecedores está vazia!')
        else:
            print('##### FORNECEDORES #####')
            for i in lista_fornecedor:
                print(f'Fornecedor: {i.nome}')
                print(f'Categoria: {i.categoria}')
                print(f'Telefone: {i.telefone}')
                print(f'CNPJ: {i.cnpj}')
                print('--------------------')


class ControllerClientes:
    def cadastrarCliente(self, nome, telefone, cpf, email, endereco):
        lista_clientes = DaoPessoa.ler()
        filtra_cpf = list(filter(lambda x: x.cpf == cpf, lista_clientes))
        if len(filtra_cpf) > 0:
            print('CPF já existe!')
        else:
            if len(cpf) == 11 and len(telefone) >= 10 and len(telefone) <= 11:
                DaoPessoa.salvar(Pessoa(nome, telefone, cpf, email, endereco))
                print('Cliente cadastrado com sucesso!')
            else:
                print('Digite um cpf ou telefone válido!')
    
    def alterarCliente(self, nomeAlterar, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco):
        lista_clientes = DaoPessoa.ler()
        filtra_cliente = list(filter(lambda x: x.nome == nomeAlterar, lista_clientes))
        if len(filtra_cliente) > 0:
            lista_clientes = list(map(lambda x: Pessoa(novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco) if(x.nome == nomeAlterar) else(lista_clientes), lista_clientes))
        else:
            print('O cliente que deseja alterar não exite!')
        with open('clientes.txt', 'w') as arq:
            for i in lista_clientes:
                arq.writelines(i.nome + '|' + i.telefone + '|' + i.cpf + '|' + i.email + '|' + i.endereco)
                arq.writelines('\n')
            print('Cliente alterado com sucesso!')
    
    def removerCliente(self, nome):
        lista_cliente = DaoPessoa.ler()
        filtra_cliente = list(filter(lambda x: x.nome == nome, lista_cliente))
        if len(filtra_cliente) > 0:
            for i in range(len(lista_cliente)):
                if lista_cliente[i].nome == nome:
                    del lista_cliente[i]
                    break
        else:
            print('O cliente que deseja remover não existe!')
            return None

        with open('clientes.txt', 'w') as arq:
            for i in lista_cliente:
                arq.writelines(i.nome + '|' + i.telefone + '|' + i.cpf + '|' + i.email + '|' + i.endereco)
                arq.writelines('\n')
            print('Cliente removido com sucesso!')
    
    def mostrarClientes(self):
        lista_cliente = DaoPessoa.ler()
        if len(lista_cliente) == 0:
            print('A lista de clientes está vazia!')
        else:
            print('##### CLIENTES #####')
            for i in lista_cliente:
                print(f'Nome: {i.nome}')
                print(f'Telefone: {i.telefone}')
                print(f'E-mail: {i.email}')
                print(f'CPF: {i.cpf}')
                print('--------------------')


class ControllerFuncionario:
    def cadastrarFuncionario(self, clt, nome, telefone, cpf, email, endereco):
        lista_funcionario = DaoFuncionario.ler()
        filtra_cpf = list(filter(lambda x: x.cpf == cpf, lista_funcionario))
        filtra_clt = list(filter(lambda x: x.clt == clt, lista_funcionario))
        if len(filtra_cpf) > 0:
            print('O CPF já existe!')
        elif len(filtra_clt) > 0:
            print('Já existe um funcionário com essa CLT cadastrada!')
        else:
            if len(cpf) == 11 and len(telefone) >= 10 and len(telefone) <= 11:
                DaoFuncionario.salvar(Funcionario(clt, nome, telefone, cpf, email, endereco))
                print('Funcionario cadastrado com sucesso!')
            else:
                print('Digite um CPF ou telefone válido!')

    def alterarFuncionario(self, nomeAlterar, novaClt, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco):
        lista_funcionario = DaoFuncionario.ler()
        filtra_funcionario = list(filter(lambda x: x.nome == nomeAlterar, lista_funcionario))
        if len(filtra_funcionario) > 0:
            lista_funcionario = list(map(lambda x: Funcionario(novaClt, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco) if(x.nome == nomeAlterar) else(lista_funcionario), lista_funcionario))
        else:
            print('O funcionario que deseja alterar não existe!')
        with open('funcionarios.txt', 'w') as arq:
            for i in lista_funcionario:
                arq.writelines(i.clt + '|' + i.nome + '|' + i.telefone + '|' + i.cpf + '|' + i.email + '|' + i.endereco)
                arq.writelines('\n')
            print('Funcionario alterado com sucesso!')

    def removerFuncionario(self, nome):
        lista_funcionario = DaoFuncionario.ler()
        filtra_funcionario = list(filter(lambda x: x.nome == nome, lista_funcionario))
        if len(filtra_funcionario) > 0:
            for i in range(len(lista_funcionario)):
                if lista_funcionario[i].nome == nome:
                    del lista_funcionario[i]
                    break
        else:
            print('O funcionario que deseja remover não existe!')
            return None
        with open('funcionarios.txt', 'w') as arq:
            for i in lista_funcionario:
                arq.writelines(i.clt + '|' + i.nome + '|' + i.telefone + '|' + i.cpf + '|' + i.email + '|' + i.endereco)
                arq.writelines('\n')
            print('Funcionario removido com sucesso!')

    def mostrarFuncionarios(self):
        lista_funcionario = DaoFuncionario.ler()
        if len(lista_funcionario) == 0:
            print('A lista de funcionarios está vázia!')
        else:
            print('##### FUNCIONÁRIOS #####')
            for i in lista_funcionario:
                print(f'Nome: {i.nome}')
                print(f'Telefone: {i.telefone}')
                print(f'Email: {i.email}')
                print(f'Endereco: {i.endereco}')
                print(f'CPF: {i.cpf}')
                print(f'CLT: {i.clt}')
                print('--------------------')
