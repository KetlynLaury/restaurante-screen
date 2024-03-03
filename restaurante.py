import os

restaurantes = [
    {'nome': 'Happy', 'categoria': 'Pizzaria', 'ativo': False},
    {'nome': 'Japita', 'categoria': 'Japonesa', 'ativo': False},
    {'nome': 'Burguer King', 'categoria': 'Fast Food', 'ativo': False},
]

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
          APP RESTAURANTE
""")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def cadastrar_restaurante():
    os.system('cls')
    print ('Cadastrar restaurante')
    nome_restaurante = input('Nome do restaurante: ')
    categoria_restaurante = input(f'Categoria do restaurante: {nome_restaurante}')

    dados_restaurante = {'nome': nome_restaurante, 'categoria': categoria_restaurante, 'ativo': False}
    restaurantes.append(dados_restaurante)

    print(f'Restaurante {nome_restaurante} cadastrado com sucesso!\n')
    input ('Pressione enter para voltar ao menu principal')
    main()

def listar_restaurantes():
    os.system('cls')
    print('Listando os restaurantes')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo_restaurante = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- {nome_restaurante} | {categoria_restaurante} | ativo: {ativo_restaurante}')

    input ('\n Pressione enter para voltar ao menu principal')
    main()

def ativar_restaurante():
    os.system('cls')
    print('Ativar restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    encontrado = False

    for restaurante in restaurantes: 
        if nome_restaurante == restaurante['nome']:
            encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)  

    if not encontrado: 
        print('O restaurante não foi encontrado')
            

    input ('\n Pressione enter para voltar ao menu principal')
    main()

def finalizar_app():
    os.system('cls')
    print('Finalizando o app')


def escolher_opcao():
    opcao_escolhida = int(input('Escolha uma opção: '))

    if opcao_escolhida == 1: 
        cadastrar_restaurante()
    elif opcao_escolhida == 2: 
        listar_restaurantes()
    elif opcao_escolhida == 3: 
        ativar_restaurante()
    else: 
        finalizar_app()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()