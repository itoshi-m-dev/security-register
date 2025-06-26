import csv
from pathlib import Path
import random
import string

ARQUIVO_FUNCIONARIOS_CSV = Path(__file__).parent / 'funcionarios.csv'
ARQUIVO_USUARIOS_CSV = Path(__file__).parent / 'usuarios.csv'

random = random.SystemRandom()

nome_funcionarios = input('Digite o nome do funcionario:')
letra_do_nome = list(nome_funcionarios)
partes = nome_funcionarios.strip().lower().split()

if len(partes) >= 2:
    username = f'{partes[0]}.{partes[-1]}'
else:
    username = partes[0]

password = random.choices(string.ascii_letters + string.digits + string.punctuation, k=12)
password_formatada = ''.join(password)
print(password_formatada)






with open(ARQUIVO_USUARIOS_CSV, 'a') as f:
    campos = ['nome','usuario','senha']
    escritor = csv.DictWriter(f,campos)
    escritor.writeheader()
    