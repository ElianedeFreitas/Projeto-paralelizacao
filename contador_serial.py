import pandas as pd
import time
import string
from collections import Counter

# =========================================
# FUNÇÃO PARA PROCESSAR TEXTO
# =========================================
def processar_texto(texto):

    texto = texto.lower()

    texto = texto.translate(
        str.maketrans('', '', string.punctuation)
    )

    palavras = texto.split()

    return palavras

# =========================================
# FUNÇÃO PRINCIPAL
# =========================================
def contar_palavras_serial(arquivo):

    print("Iniciando processamento...\n")

    inicio = time.time()

    # leitura parquet
    df = pd.read_parquet(arquivo)

    contador_total = Counter()

    total_palavras = 0

    # =====================================
    # PROCESSA LINHA POR LINHA
    # =====================================
    for texto in df["text"].astype(str):

        palavras = processar_texto(texto)

        contador_total.update(palavras)

        total_palavras += len(palavras)

    fim = time.time()

    tempo_execucao = fim - inicio

    top_10 = contador_total.most_common(10)

    # =====================================
    # RESULTADOS
    # =====================================
    print("========== RESULTADOS ==========\n")

    print(f"Total de palavras: {total_palavras}\n")

    print(f"Tempo de execução: {tempo_execucao:.2f} segundos\n")

    print("Top 10 palavras:\n")

    for palavra, quantidade in top_10:
        print(f"{palavra} -> {quantidade}")

# =========================================
# EXECUÇÃO
# =========================================

arquivo = "a.parquet"

contar_palavras_serial(arquivo)