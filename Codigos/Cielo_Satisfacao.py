import os
import pandas as pd
import shutil
import re

def adicionar_underline(texto):
    #df = pd.read_excel(url_df,sheet_name="Planilha3")
    if isinstance(texto, str):  # Verifica se o valor é uma string
        return re.sub(r'([a-z])([A-Z])', r'\1_\2', texto)
    return texto

# Caminhos
caminho_audios = r"C:\PROJETOS\Renomear_audios_py\Rayner\Audios Marco NOVO"
arquivo_excel = r"C:\PROJETOS\Renomear_audios_py\Rayner\Renomear-Audios\Dados\EMP_Cielo Satisfacao_MAR25_2025.04.28__RAYNER - v2.xlsx"

# Carregar o Excel
pd.set_option('display.float_format', '{:.0f}'.format)
# df = pd.read_excel(arquivo_excel, sheet_name="BANCO FINALIZADO")
df = pd.read_excel(arquivo_excel, sheet_name="BANCO FINALIZADO CATI")
print(df)

# nets = ['Atendimento']
# df[nets] = df[nets].applymap(adicionar_underline)


# #=== Código para renomear arquivos com o nome no seguinte formato: "211277750_MercadoPago_Promotor.mp3" (Campo) ===#
# arquivos = os.listdir(caminho_audios)
# count_renomeados = 0
# for arquivo in arquivos:
#     if arquivo.endswith(".mp3"):
#         caminho_subarquivos = os.path.join(caminho_audios, arquivo)
#         if '_' in arquivo:
#             lista_nomes = arquivo.split("_")
#             # print(f'\nlista_nomes:\t{lista_nomes}')
#             ID = lista_nomes[0]
#             ID = os.path.splitext(ID)[0]
#             ID = ID.lower()
#             # print(f'ID: {ID}')
#             Credenciadora = lista_nomes[1]
#             Credenciadora = os.path.splitext(Credenciadora)[0]
#             Credenciadora = Credenciadora.lower()
#             # print(f'Credenciadora: {Credenciadora}')

#         else:
#             lista_nomes = arquivo.split(" - ")
#             # print(f'\nlista_nomes:\t{lista_nomes}')
#             ID = lista_nomes[0]
#             ID = os.path.splitext(ID)[0]
#             ID = ID.lower()
#             # print(f'ID: {ID}')
#             Credenciadora = lista_nomes[1]
#             Credenciadora = os.path.splitext(Credenciadora)[0]
#             Credenciadora = Credenciadora.lower()
#             # print(f'Credenciadora: {Credenciadora}')
        
#     else:
#         continue 

#     try:
#         for index, row in df.astype(str).iterrows():
#             # Verificar se o nome está em uma das três colunas
#             if ID == row['ID_ONDA_CAMPO'] and Credenciadora == row['Credenciadora']:
#                 print(f'\nID: {ID}')
#                 print(f'Credenciadora: {Credenciadora}')

#                 novo_nome = f"{row['Credenciadora']}\{row['NPS']}\{row['SEG_NOVO_BU']}\{row['Credenciadora']}_{row['NPS']}_{row['SEG_NOVO_BU']}_{row['NET']}_{row['ID_ONDA_CAMPO']}.mp3"
#                 novo_caminho = os.path.join(caminho_audios, novo_nome)

#                 # Criar diretórios se necessário
#                 os.makedirs(os.path.dirname(novo_caminho), exist_ok=True)

#                 # Evitar sobrescrever arquivos existentes
#                 contador = 1
#                 while os.path.exists(novo_caminho):
#                     novo_nome = f"{row['Credenciadora']}\{row['NPS']}\{row['SEG_NOVO_BU']}\{row['Credenciadora']}_{row['NPS']}_{row['SEG_NOVO_BU']}_{row['NET']}_{row['ID_ONDA_CAMPO']}_{contador}.mp3"
#                     novo_caminho = os.path.join(caminho_audios, novo_nome)
#                     contador += 1

#                 # Renomear o arquivo
#                 os.rename(caminho_subarquivos,novo_caminho)

#                 count_renomeados += 1
            
#         else:
#             print(f"Arquivo {arquivo} não renomeado. ID extraído: {ID}, Credenciadora extraída: {Credenciadora}")
    
#     except Exception as e:
#         print(f"Erro inesperado {e=}, {type(e)=}")

# print(f"Contagem de renomeados: {count_renomeados}")


#================================================================================================================================#



#=== Código para renomear arquivos com o nome no seguinte formato: "gravacao_1120315658_800_59427_NEG_20241127152236" (Cati) ===#
count_renomeados = 0
arquivos = os.listdir(caminho_audios)
for arquivo in arquivos:
    if arquivo.endswith(".WAV"):
        caminho_subarquivos = os.path.join(caminho_audios, arquivo)
        lista_nomes = arquivo.split("_")
        print(f'\nlista_nomes:\t{lista_nomes}')
        ID = lista_nomes[3]
        ID = os.path.splitext(ID)[0]
        print(f'ID: {ID}')
        print(f'Tamanho: {len(lista_nomes)}')
        if len(lista_nomes) >= 5:
            ATRIBUTO = lista_nomes[4]
            ATRIBUTO = os.path.splitext(ATRIBUTO)[0]
            print(f'ATRIBUTO: {ATRIBUTO}')
        else:
            ATRIBUTO = lista_nomes[2]
            ATRIBUTO = os.path.splitext(ATRIBUTO)[0]
            print(f'ATRIBUTO: {ATRIBUTO}')
    else:
        continue 

    try:
        for index, row in df.astype(str).iterrows():
            # Verificar se o nome está na coluna correta
            if ID == row['ID_ONDA'] and ATRIBUTO == row['ATRIBUTO']:
                novo_nome = os.path.join(
                    row['Credenciadora'], 
                    row['NPS'], 
                    row['SEG_NOVO_BU'], 
                    f"{row['Credenciadora']}_{row['NPS']}_{row['SEG_NOVO_BU']}_{row['NET']}_{row['ID_ONDA']}.WAV"
                )
                novo_caminho = os.path.join(caminho_audios, novo_nome)

                # Criar diretórios se necessário
                os.makedirs(os.path.dirname(novo_caminho), exist_ok=True)

                # Verificar se o arquivo ainda existe
                if not os.path.exists(caminho_subarquivos):
                    print(f"Arquivo já processado ou movido: {caminho_subarquivos}")
                    break

                # Evitar sobrescrever arquivos existentes
                contador = 1
                while os.path.exists(novo_caminho):
                    novo_nome = os.path.join(
                        row['Credenciadora'], 
                        row['NPS'], 
                        row['SEG_NOVO_BU'], 
                        f"{row['Credenciadora']}_{row['NPS']}_{row['SEG_NOVO_BU']}_{row['NET']}_{row['ID_ONDA']}_{contador}.WAV"
                    )
                    novo_caminho = os.path.join(caminho_audios, novo_nome)
                    contador += 1

                # Renomear o arquivo
                os.rename(caminho_subarquivos, novo_caminho)
                # print(f"Arquivo '{arquivo}' renomeado para '{novo_caminho}'")

                count_renomeados += 1
    
    except Exception as e:
        print(f"Erro inesperado {e=}, {type(e)=}")

print(f"Contagem de renomeados: {count_renomeados}")



