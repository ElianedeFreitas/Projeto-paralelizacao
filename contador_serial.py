import pandas as pd
import time
import string
from collections import Counter

LIMITE_ARTIGOS = 1_000_000

TABELA_TRADUCAO = str.maketrans(
    '',
    '',
    string.punctuation
)

def processar_texto(texto):

    texto = texto.lower()

    texto = texto.translate(
        TABELA_TRADUCAO
    )

    return texto.split()

def contar_serial(arquivo):

    print("Lendo base de dados...")

    df = pd.read_parquet(arquivo)

    total_artigos = len(df)

    df = df.head(LIMITE_ARTIGOS)

    print(f"Total de artigos na base: {total_artigos:,}")
    print(f"Artigos processados: {len(df):,}")

    print("\nIniciando contagem serial...")

    inicio = time.time()

    contador = Counter()

    total_palavras = 0

    for texto in df["text"]:

        palavras = processar_texto(str(texto))

        contador.update(palavras)

        total_palavras += len(palavras)

    tempo = time.time() - inicio

    print("\n========== RESULTADOS ==========\n")

    print(f"Tempo de contagem: {tempo:.2f} segundos")
    print(f"Total de palavras: {total_palavras:,}")

    print("\nTop 10 palavras:\n")

    for palavra, qtd in contador.most_common(10):

        print(f"{palavra} -> {qtd:,}")

if __name__ == "__main__":

    contar_serial("a.parquet")