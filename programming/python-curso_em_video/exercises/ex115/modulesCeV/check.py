import readline

def get_database():
    try:
        raw_database = read_database()
        return format_database(raw_database)
    except:
        raise


def read_database():
    try:
        with open('database.log', 'rt') as file:
            raw_database = file.readlines()
        return raw_database
    except:
        raise

def format_database(raw_database):
    user_data = {}
    database = []

    for item in raw_database:
        user_data['nome'], user_data['idade'] = item.strip().split(',')
        database.append(user_data.copy())

    return database


def print_database(database):
    print()
    print('--' * 30)
    print('{:^60}'.format('Database'))
    print('--' * 30)
    print('{:<30s} {:<8s}'.format('Nome Completo', 'Idade'))
    print('--' * 30)

    for user_data in database:
        user_data_print = '{:>2s} anos'.format(user_data['idade'])
        print('{:<30s} {:<8s}'.format(user_data['nome'], user_data_print))
    print('--' * 30)
