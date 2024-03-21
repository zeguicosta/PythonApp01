import os

restaurantes = [{'nome': 'UniCoffee', 'categoria': 'Café', 'ativo': True},
                {'nome': 'PizzaPrime', 'categoria': 'Pizza', 'ativo': False},
                {'nome': 'BarDoZé', 'categoria': 'Lanche', 'ativo': False}]

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
    print('3. Ativar restaurante')
    print('4. Sair\n')

def voltar():
    input('Aperte ENTER para voltar ao menu principal\n')
    main()

def opcao_invalida():
    print('Opção Inválida.\n')
    voltar()

def exibir_subtitulo(texto):
    os.system('clear')
    print(texto)
    print()

def cadastrar():
    exibir_subtitulo('------ CADASTRO DE NOVOS RESTAURANTES -----')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_restaurante)
    print(f'{nome_restaurante} cadastrado com sucesso!\n')
    voltar()

def listar():
    exibir_subtitulo('----- LISTA DE RESTAURANTES -----')
    for item in restaurantes:
        nome = item['nome']
        categoria = item['categoria']
        ativo = item['ativo']
        print(f'- {nome} | {categoria} | Ativação: {ativo}')
    voltar()

def finalizar():
    exibir_subtitulo('Finalizando o app...')

def escolher_opcao():
    try:
        opcao = int(input('Escolha uma opção: '))
        match opcao:
            case 1:
                cadastrar()
            case 2:
                listar()
            case 3:
                print('Restaurante ativado.')
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


