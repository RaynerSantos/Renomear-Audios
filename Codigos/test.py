import pandas as pd

string = 'gravacao_18997440639_NRC_20241105120808.WAV'

string = string.split("_")

print(f'Tamanho: {len(string)}')

if '-' in string:
    print('Ok')
else:
    print("Não Ok")