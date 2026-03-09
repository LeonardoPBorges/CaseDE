import requests
import os
import json
from datetime import datetime

def ingest_api_externa_local_to_specific_folder():
    
    #URL de solicitação fornecido pelo Site pro.coincap.io/api-docs/
    api_url = "https://rest.coincap.io/v3/assets?limit=100&offset=0"
    
    # Chamada da chave API
    api_key = os.environ.get("COINCAP_API_KEY") 
    
    print(f"Valor da COINCAP_API_KEY (segundo o script): {api_key}") 
    
    if not api_key:
        print("Erro: A variável de ambiente COINCAP_API_KEY não está definida.")
        print("Por favor, defina-a no seu terminal (ex: set COINCAP_API_KEY='sua_chave') ou em um arquivo .env")
        return # Termina a execução da função

    headers = {"Authorization": f"Bearer {api_key}"}
    
    try:
        print(f"Buscando dados da API: {api_url}")
        response = requests.get(api_url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição da API: {e}")
        return # Termina a execução da função

    json_response = response.json()

    # A API CoinCap retorna os dados de ativos sob a chave 'data'.
    # Extraímos essa lista de dicionários para salvar.
    data_to_save = json_response.get("data", []) 
    
    if not data_to_save:
        print("A API não retornou dados de ativos ou a chave 'data' está vazia. Nenhum arquivo será salvo.")
        return # Termina a execução da função

    # -------- Lógica para salvar o arquivo na pasta ---------
    try:
        
        target_folder = r"C:\Users\LEONARDOBO\Desktop\teste" # Use r"" para string raw
        
        # Garante que a pasta exista; se não, cria
        os.makedirs(target_folder, exist_ok=True)
        
        # Cria um nome de arquivo
        
        filename = f"coin_cap_assets.txt"
        full_file_path = os.path.join(target_folder, filename)

        with open(full_file_path, 'w', encoding='utf-8') as f:
            for record in data_to_save:
                # Converte cada dicionário (registro) para uma string JSON e adiciona uma nova linha
                f.write(json.dumps(record, ensure_ascii=False) + '\n')
        
        print(f"Dados salvos com sucesso como Newline-Delimited JSON em: {full_file_path}")
        print(f"Número de registros salvos: {len(data_to_save)}")

    except Exception as e:
        print(f"Erro ao salvar o arquivo na pasta: {e}")
        print("Verifique se o caminho da pasta está correto e se há permissão de escrita.")

# Chama a função para execução quando o script é rodado
if __name__ == "__main__":
    ingest_api_externa_local_to_specific_folder()

