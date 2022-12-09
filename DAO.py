from models import *

class DaoCategoria:
    @classmethod
    def salvar(cls, categoria):
        with open('categoria.txt', 'a') as arq:
            arq.writelines(categoria) # ESCREVE NO ARQUIVO OS PARAMETROS PASSADOS NA CLASS CATEGORIA DA MODELS
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('categoria.txt', 'r') as arq:
            cls.categoria = arq.readlines() # PASSA PARA UMA VARIÁVEL A LEITURA DAS LINHAS DO ARQUIVO
        cls.categoria = list(map(lambda x: x.replace('\n', ''), cls.categoria)) # RETIRA O \n DO ARQUIVO
        cat = []
        for i in cls.categoria:
            cat.append(Categoria(i)) # ADICIONA AS CATEGORIAS DO ARQUIVO DENTRO DE UMA LISTA PARA SEREM MOSTRADAS NO TERMINAL
        return cat # RETORNA UMA LISTA COM AS CATEGORIAS


class DaoVenda:
    @classmethod
    def salvar(cls, venda: Venda):
        with open('venda.txt', 'a') as arq:
            arq.writelines(venda.itensVendidos.nome + '|' +
                            venda.itensVendidos.preco + '|' + 
                            venda.itensVendidos.categoria + '|' + 
                            venda.vendedor + '|' + venda.cliente + '|' + 
                            str(venda.quantidadeVendida) + '|' + 
                            venda.data) # ESCREVE NO ARQUIVO OS PARAMETROS PASSADOS NA CLASS VENDA DA MODEL, QUE TEM COMO PARAMENTRO UM TIPO PRODUTO DA MODEL
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('venda.txt', 'r') as arq:
            cls.venda = arq.readlines()
        cls.venda = list(map(lambda x: x.replace('\n', ''), cls.venda))
        cls.venda = list(map(lambda x: x.split('|'), cls.venda)) # SEPARA PELO CARACTER OS ITENS EM UMA LISTA
        vend = []
        for i in cls.venda:
            vend.append(Venda(Produtos(i[0], i[1], i[2]), i[3], i[4], i[5], i[6])) # 0=NOME, 1=PRECO, 2=CATEGORIA, 3=VENDEDOR, 4=CLIENTE, 5=QUANTIDADEVENDIDA, 6=DATA
        return vend # RETORNA UMA LISTA COM AS VENDAS


class DaoEstoque:
    @classmethod
    def salvar(cls, produto: Produtos, quantidade):
        with open('estoque.txt', 'a') as arq:
            arq.writelines(produto.nome + '|' +
                            produto.preco + '|' +
                            produto.categoria + '|' +
                            str(quantidade))
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('estoque.txt', 'r') as arq:
            cls.estoque = arq.readlines()
        cls.estoque = list(map(lambda x: x.replace('\n', ''), cls.estoque))
        cls.estoque = list(map(lambda x: x.split('|'), cls.estoque))
        est = []
        if len(cls.estoque) > 0:
            for i in cls.estoque:
                est.append(Estoque(Produtos(i[0], i[1], i[2]), int(i[3])))
        return est


class DaoFornecedor:
    @classmethod
    def salvar(cls, fornecedor: Fornecedor):
        with open('fornecedores.txt', 'a') as arq:
            arq.writelines(fornecedor.nome + '|' +
                            fornecedor.cnpj + '|' +
                            fornecedor.telefone + '|' +
                            fornecedor.categoria)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('fornecedores.txt', 'r') as arq:
            cls.fornecedores = arq.readlines()
        cls.fornecedores = list(map(lambda x: x.replace('\n', ''), cls.fornecedores))
        cls.fornecedores = list(map(lambda x: x.split('|'), cls.fornecedores))
        forn = []
        for i in cls.fornecedores:
            forn.append(Fornecedor(i[0], i[1], i[2], i[3]))
        return forn 


class DaoPessoa:
    @classmethod
    def salvar(cls, pessoas: Pessoa):
        with open('clientes.txt', 'a') as arq:
            arq.writelines(pessoas.nome + '|' +
                            pessoas.telefone + '|' +
                            pessoas.cpf + '|' +
                            pessoas.email + '|' +
                            pessoas.endereco)
            arq.writelines('\n')
    
    @classmethod
    def ler(cls):
        with open('clientes.txt', 'r') as arq:
            cls.clientes = arq.readlines()
        cls.clientes = list(map(lambda x: x.replace('\n', ''), cls.clientes))
        cls.clientes = list(map(lambda x: x.split('|'), cls.clientes))
        clientes = []
        for i in cls.clientes:
            clientes.append(Pessoa(i[0], i[1], i[2], i[3], i[4]))
        return clientes


class DaoFuncionario:
    @classmethod
    def salvar(cls, funcionario: Funcionario):
        with open('funcionarios.txt', 'a') as arq:
            arq.writelines(funcionario.clt + '|' +
                            funcionario.nome + '|' +
                            funcionario.telefone + '|' +
                            funcionario.cpf + '|' +
                            funcionario.email + '|' +
                            funcionario.endereco)
            arq.writelines('\n')
    
    @classmethod
    def ler(cls):
        with open('funcionarios.txt', 'r') as arq:
            cls.funcionarios = arq.readlines()
        cls.funcionarios = list(map(lambda x: x.replace('\n', ''), cls.funcionarios))
        cls.funcionarios = list(map(lambda x: x.split('|'), cls.funcionarios))
        funcionario = []
        for i in cls.funcionarios:
            funcionario.append(Funcionario(i[0], i[1], i[2], i[3], i[4], i[5]))
        return funcionario
