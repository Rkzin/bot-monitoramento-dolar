# 🤖 Bot de Monitoramento de Câmbio (ETL)

Este projeto é uma automação desenvolvida em Python que monitora a cotação do Dólar em tempo real e gera relatórios históricos automaticamente em Excel.

## 🎯 Objetivo
Demonstrar a aplicação prática de Python para Engenharia de Dados básica:
1. **Extract (Extração):** Consumo de API pública de finanças.
2. **Transform (Transformação):** Tratamento de dados (JSON para Tabular) e formatação numérica (Padrão PT-BR).
3. **Load (Carga):** Armazenamento incremental em arquivo CSV compatível com Excel.

## 🛠️ Tecnologias Utilizadas
* **Python 3.14**
* **Requests:** Para comunicação HTTP.
* **Pandas:** Para manipulação de dados e criação das tabelas.
* **OpenPyXL:** Para integração com planilhas.
* **OS/DateTime:** Para gerenciamento de arquivos e carimbos de tempo.

## 🚀 Como funciona
O script roda em loop infinito, verificando a cotação a cada 10 segundos. Se o arquivo Excel não existir, ele cria. Se já existir, ele adiciona a nova linha sem apagar o histórico anterior.

## 📸 Resultado
*(Aqui você vai colocar a imagem do Excel que você me mandou)*
