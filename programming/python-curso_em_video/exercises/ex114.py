import requests

url = 'http://www.pudim.com.br'
try:
    requests.get(url)
except requests.exceptions.ConnectionError:
    print('\033[91m' + 'O site {} não se encontra acessível.'.format(url) + '\033[m')
else:
    print('\033[92m' + 'O site {} se encontra acessível.'.format(url) + '\033[m')
