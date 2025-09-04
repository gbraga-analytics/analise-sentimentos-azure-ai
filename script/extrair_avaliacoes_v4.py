import os
import re
import pandas as pd
from bs4 import BeautifulSoup

# Contadores p/diagnóstico
total_paineis = 0
total_sem_comentario = 0

# Detecta a pasta base do projeto automaticamente
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PASTA_HTML = os.path.join(BASE_DIR, "data", "html_paginas")
ARQUIVO_SAIDA = os.path.join(BASE_DIR, "data", "avaliacoes_duo_gourmet.csv")

def limpar_texto(texto):
    if not texto:
        return ""
    # Remove "?" que substituem emojis
    texto = texto.replace("?", "")
    # Remove espaços e quebras de linha extras
    texto = re.sub(r'\s+', ' ', texto).strip()
    return texto

def anonimizar_nome(numero):
    return f"[cliente{numero}]"

dados = []
id_counter = 1

for arquivo in os.listdir(PASTA_HTML):
    if arquivo.endswith(".html"):
        with open(os.path.join(PASTA_HTML, arquivo), "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, "lxml")
            panels = soup.find_all("div", class_="panel panel-default")
            total_paineis += len(panels)  # soma total de painéis encontrados no arquivo

            for panel in panels:
                nome = panel.find("h3", class_="panel-title").get_text(strip=True)
                nota = panel.find("div", class_="pull-right star").get_text(strip=True)
                comentario_raw = panel.find("div", class_="panel-body").get_text(strip=True)
                data_raw = panel.find("div", class_="panel-footer").get_text(strip=True)

                # Ignora avaliações sem comentário
                if "Avaliação sem comentário" in comentario_raw:
                    total_sem_comentario += 1
                    continue

                comentario = limpar_texto(comentario_raw)
                data = limpar_texto(data_raw.split("Pedido")[0])
                cliente_anonimo = anonimizar_nome(id_counter)  # anonimiza os feedbacks

                dados.append({
                    "id": id_counter,
                    "cliente": cliente_anonimo,
                    "comentario": comentario,
                    "data": data,
                    "nota": nota
                })
                id_counter += 1

# Salva no CSV
df = pd.DataFrame(dados)
df.to_csv(ARQUIVO_SAIDA, index=False, encoding="utf-8")

print(f"Painéis encontrados: {total_paineis}")
print(f"Avaliações sem comentário: {total_sem_comentario}")
print(f"Avaliações com comentário: {len(dados)}")
print(f"✅ Extração concluída! {len(dados)} comentários salvos em {ARQUIVO_SAIDA}")