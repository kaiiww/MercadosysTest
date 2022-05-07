from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import formata_float_str_moeda

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []


def main() -> None:
    menu()


def menu() -> None:
    print(36*'⊹')
    print(12*'⊹', "bem vindo/a", 12*'⊹')
    print(11*'⊹', 'sei la oq shop', 11*'⊹')
    print(36 * '⊹')

    print('selecione uma opção abaixo: ')
    print('1 - cadastrar produto ')
    print('2 - listar produtos ')
    print('3 - comprar produtos ')
    print('4 - visualizar carrinho ')
    print('5 - fechar pedido ')
    print('6 - sair do sistema ')

    opcao: int = int(input())
    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produto()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print('volte sempre')
        sleep(4)
        exit(0)
    else:
        print('opcao invalida')
        sleep(3)
        menu()
    pass


def cadastrar_produto() -> None:
    print('cadastro de produto\n')
    nome: str = input('informe o nome do produto:')
    preco: float = float((input('informe o preco do produto: ')))

    produto: Produto = Produto(nome, preco)
    produtos.append(produto)
    print(f' o {produto.nome} acaba de ser cadastrado')
    sleep(3)

    menu()


def listar_produto() -> None:
    if len(produtos) > 0:
        print('lista de produtos')
        for produto in produtos:
            print(produto)
            print('-----------------')
            sleep(1)
        pass
    else:
        print(' ainda nao existem produtos cadastrados')
    sleep(1.3)
    menu()


def comprar_produto() -> None:
    if len(produtos) > 0:
        print('Informe o codigo do produto que deseja adicionar no carrinho')
        for produto in produtos:
            print(produto)
            sleep(1)
        codigo: int = int(input())
        produto: Produto = pega_produto_codigo(codigo)
        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False
                for item in carrinho:
                    quant: int = item.get(produto)
                    if quant:
                        item[produto] = quant + 1
                        print(f'o produto {produto.nome} agora possui {quant + 1} unidades no carrinho.')
                        tem_no_carrinho = True
                        sleep(1)
                if not tem_no_carrinho:
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(f'o produto {produto.nome} foi adicionado ao carrinho')
                    sleep(1.3)
                    menu()
            else:
                item = {produto: 1}
                carrinho.append(item)
                print(f' o produto {produto.nome} foi adicionado')
                sleep(1)
                menu()
        else:
            print('esse produto nao foi encontrado')
    else:
        print('sem produtos cadastrados.')
    sleep(3)
    menu()


def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print('produtos no carrinho:')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'quantidade: {dados[1]}')
                sleep(1)
    else:
        print('voce ainda nao adicionou nenhum produto no carrinho')
    sleep(3)
    menu()


def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0

        print(' Produtos do carrinho ')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'quantidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                sleep(1)
            print(f'sua fatura é {formata_float_str_moeda(valor_total)}')
            print('volte sempre')
            carrinho.clear()
    else:
        print('ainda nao tem produtos no carrinho')
    sleep(3)
    menu()


def pega_produto_codigo(codigo: int) -> Produto:
    p: Produto = None
    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p


if __name__ == '__main__':
    main()
