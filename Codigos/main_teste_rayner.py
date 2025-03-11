import pandas as pd
import os
import re

def adicionar_underline(texto):
    #df = pd.read_excel(url_df,sheet_name="Planilha3")
    if isinstance(texto, str):  # Verifica se o valor é uma string
        return re.sub(r'([a-z])([A-Z])', r'\1_\2', texto)
    return texto
    

def renomaer_arquivos(caminho_arquvios, url_df):
    arquivos = os.listdir(caminho_arquvios)
    pd.set_option('display.float_format', '{:.0f}'.format)
    df = pd.read_excel(url_df,sheet_name="Tabela_tratada")
    
    nets = ['Valor']

    df[nets] = df[nets].applymap(adicionar_underline)

    for arquivo in arquivos:
        if arquivo.endswith(".WAV"):
            caminho_subarquivos = os.path.join(caminho_arquvios, arquivo)
            nome_completo = os.path.basename(caminho_subarquivos)
            nome = nome_completo.split("_")[1]
            extensao = os.path.splitext(nome_completo)[1]

        else:
            continue
        try:
            for index, row in df.astype(str).iterrows():
                # Verificar se o nome está em uma das três colunas
                if nome == row['TEL_FEITO'] or nome == row['FONE1'] or nome == row['FONE2']:
                    
                    novo_nome = f"{row['Atributo']}\{row['ID_EMP']}_{row['VSEG']}_{row['Atributo']}_{row['Valor']}.WAV"
                    novo_caminho = os.path.join(caminho_arquvios,novo_nome)

                    os.rename(caminho_subarquivos,novo_caminho)            
        except Exception as e:
            print(f"Unexpected {e=}, {type(e)=}")

def renomaer_arquivos_all(caminho_arquvios, url_df):

    pd.set_option('display.float_format', '{:.0f}'.format)
    df = pd.read_excel(url_df,sheet_name="Tabela_tratada")
    print(df.head())
    
    nets = ['Valor']

    df[nets] = df[nets].applymap(adicionar_underline)
    print(df[nets])

    lista_paths = os.listdir(caminho_arquvios)

    for path in lista_paths:
        caminho_path = os.path.join(caminho_arquvios,path)
        print(f'\ncaminho_path:\t{caminho_path}')

        # Verificar se é um diretório antes de listar os arquivos
        if os.path.isdir(caminho_path):
            arquivos = os.listdir(caminho_path)
            print(f'tamanho_arquivos:\t{len(arquivos)}')
            if len(arquivos) > 0:
                for arquivo in arquivos:
                    if arquivo.endswith(".WAV"):
                        caminho_subarquivos = os.path.join(caminho_path, arquivo)
                        nome_completo = os.path.basename(caminho_subarquivos)
                        print(f'nome_completo:\t{nome_completo}')
                        nome_completo_separado = nome_completo.split("_")
                        print(f'nome_completo_separado:\t{nome_completo_separado}')
                        if 'Q20' in nome_completo_separado:
                            continue

                        nome = nome_completo_separado[1]
                        extensao = os.path.splitext(nome_completo)[1]

                    else:
                        continue
                    try:
                        for index, row in df.astype(str).iterrows():
                            # Verificar se o nome está em uma das três colunas
                            if nome == row['TEL_FEITO'] or nome == row['FONE1'] or nome == row['FONE2']:
                                
                                novo_nome = f"{row['Atributo']}\{row['ID_EMP']}_{row['VSEG']}_{row['Atributo']}_{row['Valor']}.WAV"
                                novo_caminho = os.path.join(caminho_arquvios,novo_nome)
                                os.rename(caminho_subarquivos,novo_caminho)
                    except Exception as e:
                        print(f"Unexpected {e=}, {type(e)=}")
            else:
                continue
        else:
            print(f"'{caminho_path}' não é um diretório. Ignorando...")

# df = r"C:\Users\mairon.costa\OneDrive - Expertise Inteligência e Pesquisa de Mercado\expertise_mairon\2024\Cielo_NPS_cortes\Base de dados\BD_Cielo NPS Mensal_SET24.xlsx"
# url = r'C:\Users\mairon.costa\OneDrive - Expertise Inteligência e Pesquisa de Mercado\expertise_mairon\2024\Cielo_NPS_cortes\teste\09'

df = r"C:\PROJETOS\Renomear_audios_py\cielo\cielo_com_underline\auto_Cielo_renomear\dados\bd_teste_rayner.xlsx"
url = r"C:\PROJETOS\Renomear_audios_py\cielo\cielo_com_underline\Teste"


#renomaer_arquivos(url,df)
renomaer_arquivos_all(url,df)