from modulesCeV import register, check

def print_header():
    print('=-' * 30)
    print('{:^60}'.format('MENU PRINCIPAL'))
    print('=-' * 30)


def print_options():
    options = {'1': 'Ver pessoas cadastradas',
               '2': 'Cadastrar uma nova pessoa',
               '3': 'Sair do sistema'}

    for num, opt in options.items():
        print('\033[93m{} -\033[m \033[94m{}\033[m'.format(num, opt))

    print('=-' * 30)


def get_input():
    while True:
        try:
            user_input = str(input('\033[93mSua Opção: \033[m')).strip()[0]
            test_input(user_input)
            return user_input
        except:
            print('\033[91mO valor {} não é válido.\033[m'.format(user_input))


def test_input(user_input):
    if user_input not in ['1', '2', '3']:
        raise


def run_module(user_input):
    def check_proc():
        try:
            database = check.get_database()
        except FileNotFoundError:
            print('\033[91m> Ainda não possuímos uma database cadastrada.\033[m')
        else:
            check.print_database(database)

    def register_proc():
        register.write_database()

    def end_proc():
        global running_status
        print('\033[91m{:^60}\033[m'.format('Obrigado por usar nosso programa!'))
        running_status = False

    def create_menu_option():

        menu_option = { '1': check_proc,
                        '2': register_proc,
                        '3': end_proc}
        return menu_option

    menu_option = create_menu_option()
    menu_option[user_input]()


# Main Menu
running_status = True

while running_status:
    print_header()
    print_options()
    user_input = get_input()
    run_module(user_input)