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
caminho_audios = r"C:\PROJETOS\Renomear_audios_py\Rayner\Audios Abril"
arquivo_excel = r"C:\PROJETOS\Renomear_audios_py\Rayner\Renomear-Audios\Dados\BD_Cielo_NPS_Abril25_2025.05.12.xlsx"

# Carregar o Excel
pd.set_option('display.float_format', '{:.0f}'.format)
df = pd.read_excel(arquivo_excel, sheet_name="BANCO FINALIZADO")
# df = pd.read_excel(arquivo_excel, sheet_name="BANCO FINALIZADO CATI")
print(df)

# nets = ['Atendimento']
# df[nets] = df[nets].applymap(adicionar_underline)


# #=== Código para renomear arquivos com o nome no seguinte formato: "gravacao_1120315658_800_59427_NEG_20241127152236" (Cati) ===#
# arquivos = os.listdir(caminho_audios)
# for arquivo in arquivos:
#     if arquivo.endswith(".mp3"):
#         caminho_subarquivos = os.path.join(caminho_audios, arquivo)
#         lista_nomes = arquivo.split("_")
#         print(f'\nlista_nomes:\t{lista_nomes}')
#         print(f'Tamanho: {len(lista_nomes)}')
#         if len(lista_nomes) >= 2:
#             ID = lista_nomes[0]
#             ID = os.path.splitext(ID)[0]
#             print(f'ID: {ID}')
#             # ATRIBUTO = lista_nomes[4]
#             # ATRIBUTO = os.path.splitext(ATRIBUTO)[0]
#             # print(f'ATRIBUTO: {ATRIBUTO}')
#         else:
#             ID = lista_nomes[1]
#             ID = os.path.splitext(ID)[0]
#             print(f'ID: {ID}')
#             # ATRIBUTO = lista_nomes[2]
#             # ATRIBUTO = os.path.splitext(ATRIBUTO)[0]
#             # print(f'ATRIBUTO: {ATRIBUTO}')
#     else:
#         continue 

#     try:
#         for index, row in df.astype(str).iterrows():
#             # Verificar se o nome está na coluna correta
#             if ID == row['ID_ONDA']: # and ATRIBUTO == row['Atributo']:
#                 novo_nome = os.path.join(
#                     # row['Credenciadora'], 
#                     row['Class_NPS'], 
#                     row['VSEG_1'], 
#                     f"{row['Class_NPS']}_{row['VSEG_1']}_{row['NET']}_{row['ID_ONDA']}.mp3"
#                 )
#                 novo_caminho = os.path.join(caminho_audios, novo_nome)

#                 # Criar diretórios se necessário
#                 os.makedirs(os.path.dirname(novo_caminho), exist_ok=True)

#                 # Verificar se o arquivo ainda existe
#                 if not os.path.exists(caminho_subarquivos):
#                     print(f"Arquivo já processado ou movido: {caminho_subarquivos}")
#                     break

#                 # Evitar sobrescrever arquivos existentes
#                 contador = 1
#                 while os.path.exists(novo_caminho):
#                     novo_nome = os.path.join(
#                         # row['Credenciadora'], 
#                         row['Class_NPS'], 
#                         row['VSEG_1'], 
#                         f"{row['Class_NPS']}_{row['VSEG_1']}_{row['NET']}_{row['ID_ONDA']}_{contador}.mp3"
#                     )
#                     novo_caminho = os.path.join(caminho_audios, novo_nome)
#                     contador += 1

#                 # Renomear o arquivo
#                 os.rename(caminho_subarquivos, novo_caminho)
#                 # print(f"Arquivo '{arquivo}' renomeado para '{novo_caminho}'")
    
#     except Exception as e:
#         print(f"Erro inesperado {e=}, {type(e)=}")




#================================================================================================================================#


# #=== Código para contar a quantidade de NS/NR e gravações não encontradas no banco ===#
# import os
# import pandas as pd

# # Caminhos
# caminho_audios = r"C:\PROJETOS\Renomear_audios_py\Rayner\Audios Fevereiro"
# arquivo_excel = r"C:\PROJETOS\Renomear_audios_py\Rayner\Renomear-Audios\Dados\BD_NPS_Mensal_Fev25.10.03.2025.xlsx"

# # Carregar o Excel
# pd.set_option('display.float_format', '{:.0f}'.format)
# df = pd.read_excel(arquivo_excel, sheet_name="Verif NS_NR", dtype=str)  # Garante que todas as colunas sejam strings

# # Criar listas das colunas que serão comparadas
# df["ID_ONDA"] = df["ID_ONDA"].str.strip()  # Remove espaços extras
# df["TEL_FEITO"] = df["TEL_FEITO"].str.strip()
# df["Valor"] = df["Valor"].str.strip()

# arquivos = os.listdir(caminho_audios)

# # Inicializar contadores
# count_NSNR = 0
# count_Nao_encontrado = 0
# count_audios_divergentes = 0
# NS_NR = []
# Nao_encontrado = []
# Audios_divergentes = []

# for arquivo in arquivos:
#     if arquivo.endswith(".WAV"):
#         lista_nomes = arquivo.split("_")
        
#         if len(lista_nomes) >= 5:
#             ID = lista_nomes[3].split(".")[0].strip()
#             ATRIBUTO = lista_nomes[4].split(".")[0].strip()
#         else:
#             ID = lista_nomes[1].split(".")[0].strip()
#             ATRIBUTO = lista_nomes[2].split(".")[0].strip()

#         print(f"ID extraído: {ID}, ATRIBUTO extraído: {ATRIBUTO}")

#         # Verificar se o ID está no DataFrame e se corresponde ao valor "NS/NR"
#         if ((df["ID_ONDA"] == ID) & (df["Valor"] == "NS/NR")).any() or \
#            ((df["TEL_FEITO"] == ID) & (df["Valor"] == "NS/NR")).any():
#             count_NSNR += 1
#             NS_NR.append(ID)
#         elif ((df["ID_ONDA"] == ID) & (df["Atributo"] != ATRIBUTO)).any() or \
#            ((df["TEL_FEITO"] == ID) & (df["Atributo"] != ATRIBUTO)).any():
#             count_audios_divergentes += 1
#             Audios_divergentes.append(ID)
#         else:
#             count_Nao_encontrado += 1
#             Nao_encontrado.append(ID)

# print(f'\nContagem de NS/NR: {count_NSNR}')
# print(f'Contagem de Não encontrado: {count_Nao_encontrado}')
# print(f'Contagem de Áudios divergentes: {count_audios_divergentes}')

# dados_para_verificar_NS_NR = pd.DataFrame({'ID_ONDA_TEL_FEITO': NS_NR})
# dados_para_verificar_Nao_encontrado = pd.DataFrame({'ID_ONDA_TEL_FEITO':Nao_encontrado})
# dados_para_verificar_Audios_divergentes = pd.DataFrame({'ID_ONDA_TEL_FEITO': Audios_divergentes})

# with pd.ExcelWriter('Verificar_audios_nao_renomeados.xlsx', engine='xlsxwriter') as writer:
#     dados_para_verificar_NS_NR.to_excel(writer, sheet_name='NS_NR', index=False)
#     dados_para_verificar_Nao_encontrado.to_excel(writer, sheet_name='Nao_encontrado', index=False)
#     dados_para_verificar_Audios_divergentes.to_excel(writer, sheet_name='Audios_divergentes', index=False)




#=== Código para contar a quantidade de NS/NR e gravações não encontradas no banco ===#
#=== Código utilizado para o banco Satisfação ===#

# Carregar o Excel
pd.set_option('display.float_format', '{:.0f}'.format)
df = pd.read_excel(arquivo_excel, sheet_name="Verif NS_NR", dtype=str)  # Garante que todas as colunas sejam strings

# Criar listas das colunas que serão comparadas
# df["ID_ONDA_CAMPO"] = df["ID_ONDA_CAMPO"].str.strip()  # Remove espaços extras
df["ID_ONDA"] = df["ID_ONDA"].str.strip()  # Remove espaços extras
df["NET"] = df["NET"].str.strip()

arquivos = os.listdir(caminho_audios)

# Inicializar contadores
count_NSNR = 0
count_audio_nao_encontrado = 0
count_audios_divergentes = 0
count_Nao_encontrado_no_banco = 0

NS_NR = []
Audio_nao_encontrado = []
Audios_divergentes = []
Nao_encontrado_no_banco = []

for arquivo in arquivos:
    if arquivo.endswith(".mp3"):
    # if arquivo.endswith(".WAV"):
        lista_nomes = arquivo.split("_")
        
        if len(lista_nomes) <= 3:
            ID = lista_nomes[0].split(".")[0].strip()
            # Credenciadora = lista_nomes[1].split(".")[0].strip()
            # ATRIBUTO = lista_nomes[4].split(".")[0].strip()
        else:
            ID = lista_nomes[0].split(".")[0].strip()
            # Credenciadora = lista_nomes[2].split(".")[0].strip()
            # ATRIBUTO = lista_nomes[4].split(".")[0].strip()

        # print(f"ID extraído: {ID}, Credenciadora extraída: {Credenciadora}")
        # print(f"ID extraído: {ID}, ATRIBUTO extraído: {ATRIBUTO}")

        # Verificar se o ID está no DataFrame e se corresponde ao valor "NS/NR"
        if ((df["ID_ONDA"] == ID) & (df["NET"] == "NS/NR")).any():
            count_NSNR += 1
            NS_NR.append(ID)
        elif ((df["ID_ONDA"] == ID) & (df["NET"] == 'Áudio não encontrado')).any():
            count_audio_nao_encontrado += 1
            Audio_nao_encontrado.append(ID)
        # elif (df["ID_ONDA"] == ID).any():
        # # elif ((df["ID_ONDA"] == ID) & (df["ATRIBUTO"] != ATRIBUTO)).any():
        #     count_audios_divergentes += 1
        #     Audios_divergentes.append(ID)
        else:
            count_Nao_encontrado_no_banco += 1
            Nao_encontrado_no_banco.append(ID)

print(f'\nContagem de NS/NR (Rose): {count_NSNR}')
print(f'Contagem de Áudios não encontrados (Rose): {count_audio_nao_encontrado}')
# print(f'Contagem de Áudios divergentes: {count_audios_divergentes}')
print(f'Contagem de ID Não encontrado no banco: {count_Nao_encontrado_no_banco}')


dados_para_verificar_NS_NR = pd.DataFrame({'ID_ONDA_TEL_FEITO': NS_NR})
dados_para_verificar_Audios_nao_encontrado = pd.DataFrame({'ID_ONDA_TEL_FEITO': Audio_nao_encontrado})
# dados_para_verificar_Audios_divergentes = pd.DataFrame({'ID_ONDA_TEL_FEITO': Audios_divergentes})
dados_para_verificar_Nao_encontrado_no_banco = pd.DataFrame({'ID_ONDA_TEL_FEITO':Nao_encontrado_no_banco})


with pd.ExcelWriter(r"C:\PROJETOS\Renomear_audios_py\Rayner\Renomear-Audios\Dados\Verificar_audios_nao_renomeados.xlsx", 
                    engine='xlsxwriter') as writer:
    dados_para_verificar_NS_NR.to_excel(writer, sheet_name='NS_NR', index=False)
    dados_para_verificar_Audios_nao_encontrado.to_excel(writer, sheet_name='Audio_Nao_encontrado', index=False)
    # dados_para_verificar_Audios_divergentes.to_excel(writer, sheet_name='Audios_divergentes', index=False)
    dados_para_verificar_Nao_encontrado_no_banco.to_excel(writer, sheet_name='ID_Nao_encontrado', index=False)
    
    