import os

restaurantes = [{'nome':'UniCoffee', 'categoria':'Café', 'ativo':True},
                {'nome':'PizzaPrime', 'categoria':'Pizza', 'ativo':False},
                {'nome':'BarDoZé', 'categoria':'Lanche', 'ativo':False}]

def exibir_titulo():
    print('''
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    ''')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado de ativação do restaurante')
    print('4. Sair\n')

def voltar():
    input('Aperte ENTER para voltar ao menu principal\n')
    main()

def opcao_invalida():
    print('Opção Inválida.\n')
    voltar()

def exibir_subtitulo(texto):
    os.system('clear')
    linha = '-' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar():
    exibir_subtitulo('|     CADASTRO DE NOVOS RESTAURANTES     |')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite a categoria de {nome_restaurante}: ')
    dados_restaurante = {'nome':nome_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_restaurante)
    print(f'{nome_restaurante} cadastrado com sucesso!\n')
    voltar()

def listar():
    exibir_subtitulo('|     LISTA DE RESTAURANTES     |')

    cabecalho = f'{'Nome do Restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Ativação'}'
    linha = '-' * (len(cabecalho) + 4)
    print(cabecalho)
    print(linha)
    for item in restaurantes:
        nome_restaurante = item['nome']
        categoria = item['categoria']
        ativo = 'Ativado' if item['ativo'] else 'Desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    
    print()
    voltar()

def ativar():
    exibir_subtitulo('|     ALTERNANDO ESTADO DE ATIVAÇÃO     |')
    nome_restaurante = input('Digite o nome do restaurante que deseja ativar/desativar: ')
    nome_verificado = False

    for item in restaurantes:
        if nome_restaurante == item['nome']:
            nome_verificado = True
            item['ativo'] = not item['ativo']
            if item['ativo']:
                mensagem = f'{nome_restaurante} ativado com sucesso!'
            else:
                mensagem = f'{nome_restaurante} desativado com sucesso!'
            print(mensagem)
    if not nome_verificado:
        print('Restaurante não encontrado.')

    print()
    voltar()

def finalizar():
    os.system('clear')
    print('Finalizando o app...')

def escolher_opcao():
    try:
        opcao = int(input('Escolha uma opção: '))
        match opcao:
            case 1:
                cadastrar()
            case 2:
                listar()
            case 3:
                ativar()
            case 4:
                finalizar()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('clear')
    exibir_titulo()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()


