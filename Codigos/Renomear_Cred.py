import os
import pandas as pd
import shutil
import re

###=== Código utilizado para o banco Satisfação ===###

caminho_audios = r"C:\PROJETOS\Renomear_audios_py\Rayner\Audios Marco"

#=== Código para renomear o nome da Credenciadora (formato: "211277750_MercadoPago_Promotor.mp3" (Campo)) ===#
arquivos = os.listdir(caminho_audios)
for arquivo in arquivos:
    if arquivo.endswith(".mp3"):
        caminho_subarquivos = os.path.join(caminho_audios, arquivo)
        if '_' in arquivo:
            lista_nomes = arquivo.split("_")
            # print(f'\nlista_nomes:\t{lista_nomes}')
            ID = lista_nomes[0]
            ID = os.path.splitext(ID)[0]
            ID = ID.lower()
            # print(f'ID: {ID}')
            Credenciadora = lista_nomes[1]
            Credenciadora = os.path.splitext(Credenciadora)[0]
            Credenciadora = Credenciadora.lower()
            # print(f'Credenciadora: {Credenciadora}')
            cat_NPS = lista_nomes[2]
            cat_NPS = os.path.splitext(cat_NPS)[0]
            # print(f'cat_NPS: {cat_NPS}')

        else:
            lista_nomes = arquivo.split(" - ")
            # print(f'\nlista_nomes:\t{lista_nomes}')
            ID = lista_nomes[0]
            ID = os.path.splitext(ID)[0]
            ID = ID.lower()
            # print(f'ID: {ID}')
            Credenciadora = lista_nomes[1]
            Credenciadora = os.path.splitext(Credenciadora)[0]
            Credenciadora = Credenciadora.lower()
            # print(f'Credenciadora: {Credenciadora}')
            cat_NPS = lista_nomes[2]
            cat_NPS = os.path.splitext(cat_NPS)[0]
        
    else:
        continue 

    try:
        if ((Credenciadora == 'infinitpay') or (Credenciadora == 'infinitypay') or (Credenciadora == 'infinite') or (Credenciadora == 'infinitipay') or (Credenciadora == 'infiniti') or (Credenciadora == 'infinetepay')): 
        # if ((Credenciadora == 'safra')):
        # if ((Credenciadora == 'pagseguros') or (Credenciadora == 'pageseguro') or (Credenciadora == 'pagdeguro')): 
        # if ((Credenciadora == 'ton')):
        # if ((Credenciadora == 'mercadopag') or (Credenciadora == 'mercado')): 
        # if ((Credenciadora == 'getnat') or (Credenciadora == 'gatnet')):
        # if ((Credenciadora == 'reede') or (Credenciadora == 'red')):
            print(f'\nID: {ID}')
            print(f'Credenciadora: {Credenciadora}')

            novo_nome = f"{ID}_infinitepay_{cat_NPS}.mp3"
            # novo_nome = f"{ID}_safrapay_{cat_NPS}.mp3"
            # novo_nome = f"{ID}_pagseguro_{cat_NPS}.mp3"
            # novo_nome = f"{ID}_stone_{cat_NPS}.mp3"
            # novo_nome = f"{ID}_mercadopago_{cat_NPS}.mp3"
            # novo_nome = f"{ID}_getnet_{cat_NPS}.mp3"
            # novo_nome = f"{ID}_rede_{cat_NPS}.mp3"
            novo_caminho = os.path.join(caminho_audios, novo_nome)

            # Renomear o arquivo
            os.rename(caminho_subarquivos, novo_caminho)
            # print(f"Arquivo '{arquivo}' renomeado para '{novo_caminho}'")
            
        else:
            print(f"Arquivo {arquivo} não renomeado. ID extraído: {ID}, Credenciadora extraída: {Credenciadora}")
    
    except Exception as e:
        print(f"Erro inesperado {e=}, {type(e)=}")