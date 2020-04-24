import readline
import sys


def write_database():
    user_data = get_user_data()
    write_user_data(user_data)
    print_message(user_data)


def get_user_data():
    user_data = {}

    while True:
        try:
            user_data['nome'] = str(input('Digite o nome: ')).strip()
        except KeyboardInterrupt:
            print('\033[91m\n>> Erro! O usuário não inseriu nenhum texto.\033[m')
        else:
            break

    while True:
        try:
            user_data['idade'] = int(input('Digite a idade: '))
        except (ValueError, TypeError):
            print('\033[91m\n> ERRO! Digite valores válidos de entrada.\033[m')
        except KeyboardInterrupt:
            print('\033[91m\n>> Erro! O usuário não inseriu nenhum texto.\033[m')
        else:
            return user_data


def write_user_data(user_data):
    with open('database.log', 'a+') as file:
        file.write('{},{}\n'.format(user_data['nome'], user_data['idade']))


def print_message(user_data):
    print('> A pessoa {} de {} anos foi cadastrada com sucesso.'.format(
        user_data['nome'], user_data['idade']))
