#=== Código para contar a quantidade de NS/NR e gravações não encontradas no banco ===#
#=== Código utilizado para o banco Satisfação ===#
import os
import pandas as pd

# Caminhos
caminho_audios = r"C:\PROJETOS\Renomear_audios_py\Rayner\Audios Marco"
arquivo_excel = r"C:\PROJETOS\Renomear_audios_py\Rayner\Renomear-Audios\Dados\EMP_Cielo Satisfacao_MAR25_2025.04.28__RAYNER.xlsx"

# Carregar o Excel
pd.set_option('display.float_format', '{:.0f}'.format)
df = pd.read_excel(arquivo_excel, sheet_name="Verif NS_NR", dtype=str)  # Garante que todas as colunas sejam strings

# Criar listas das colunas que serão comparadas
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
    # if arquivo.endswith(".mp3"):
    if arquivo.endswith(".WAV"):
        lista_nomes = arquivo.split("_")
        
        if len(lista_nomes) >= 3:
            ID = lista_nomes[3].split(".")[0].strip()
            # Credenciadora = lista_nomes[1].split(".")[0].strip()
            ATRIBUTO = lista_nomes[4].split(".")[0].strip()
        else:
            ID = lista_nomes[3].split(".")[0].strip()
            # Credenciadora = lista_nomes[2].split(".")[0].strip()
            ATRIBUTO = lista_nomes[4].split(".")[0].strip()

        print(f"ID extraído: {ID}, ATRIBUTO extraído: {ATRIBUTO}")

        # Verificar se o ID está no DataFrame e se corresponde ao valor "NS/NR"
        if ((df["ID_ONDA"] == ID) & (df["NET"] == "NS/NR")).any():
            count_NSNR += 1
            NS_NR.append(ID)
        elif ((df["ID_ONDA"] == ID) & (df["NET"] == 'Áudio não encontrado')).any():
            count_audio_nao_encontrado += 1
            Audio_nao_encontrado.append(ID)
        elif ((df["ID_ONDA"] == ID) & (df["ATRIBUTO"] != ATRIBUTO)).any():
            count_audios_divergentes += 1
            Audios_divergentes.append(ID)
        else:
            count_Nao_encontrado_no_banco += 1
            Nao_encontrado_no_banco.append(ID)

print(f'\nContagem de NS/NR (Rose): {count_NSNR}')
print(f'Contagem de Áudios não encontrados (Rose): {count_audio_nao_encontrado}')
print(f'Contagem de Não encontrado no banco: {count_Nao_encontrado_no_banco}')
print(f'Contagem de Áudios divergentes: {count_audios_divergentes}')

dados_para_verificar_NS_NR = pd.DataFrame({'ID_ONDA_TEL_FEITO': NS_NR})
dados_para_verificar_Audios_nao_encontrado = pd.DataFrame({'ID_ONDA_TEL_FEITO': Audio_nao_encontrado})
dados_para_verificar_Audios_divergentes = pd.DataFrame({'ID_ONDA_TEL_FEITO': Audios_divergentes})
dados_para_verificar_Nao_encontrado_no_banco = pd.DataFrame({'ID_ONDA_TEL_FEITO':Nao_encontrado_no_banco})


with pd.ExcelWriter(r"C:\PROJETOS\Renomear_audios_py\Rayner\Renomear-Audios\Dados\Verificar_audios_nao_renomeados.xlsx", 
                    engine='xlsxwriter') as writer:
    dados_para_verificar_NS_NR.to_excel(writer, sheet_name='NS_NR', index=False)
    dados_para_verificar_Audios_nao_encontrado.to_excel(writer, sheet_name='Audio_Nao_encontrado', index=False)
    dados_para_verificar_Audios_divergentes.to_excel(writer, sheet_name='Audios_divergentes', index=False)
    dados_para_verificar_Nao_encontrado_no_banco.to_excel(writer, sheet_name='ID_Nao_encontrado', index=False)
    
    