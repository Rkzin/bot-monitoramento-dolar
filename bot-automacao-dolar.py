import requests
import time
import pandas as pd # O padrão mundial é chamar pandas de 'pd'
from datetime import datetime
import os # Para checar se o arquivo já existe no computador

ARQUIVO = "historico_dolar.csv"

print("--- ROBÔ INICIADO: SALVANDO NO EXCEL ---")

while True:
    try:
        # 1. Pega os dados
        requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
        dados_api = requisicao.json()
        valor_bruto = float(dados_api['USDBRL']['bid'])
        
        # CORREÇÃO 1: Trocar ponto por vírgula
        # O Excel BR precisa de vírgula para entender que é número e fazer contas depois.
        valor_formatado = str(valor_bruto).replace('.', ',')

        # Pega a data e hora exata
        agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        # 2. Cria uma "mini tabela" com uma linha só
        dados_para_salvar = {
            'Data': [agora], 
            'Moeda': ['Dólar (USD)'], # Agora o acento vai funcionar
            'Valor': [valor_formatado]
        }
        
        # Transforma o dicionário em um DataFrame (Tabela do Pandas)
        tabela = pd.DataFrame(dados_para_salvar)

        # 3. Salva no Arquivo (A Mágica)
        # CORREÇÃO 2: encoding='utf-8-sig'
        # Esse é o segredo para o Excel do Windows ler acentos corretamente.
        if not os.path.isfile(ARQUIVO):
            tabela.to_csv(ARQUIVO, index=False, sep=';', encoding='utf-8-sig')
        else:
            tabela.to_csv(ARQUIVO, mode='a', header=False, index=False, sep=';', encoding='utf-8-sig')

        print(f"[{agora}] Cotação R$ {valor_formatado} salva no Excel!")

    except Exception as erro:
        print(f"Deu ruim: {erro}")

    # Espera 10 segundos pra não encher sua planilha muito rápido no teste
    time.sleep(10)