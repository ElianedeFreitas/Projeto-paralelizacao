import pandas as pd
import time
import string
from collections import Counter
from concurrent.futures import ThreadPoolExecutor

# =========================================
# CONFIGURAÇÕES
# =========================================

LIMITE_ARTIGOS = 1_000_000

CONFIGURACOES = [2, 4, 8, 12]

# Tabela criada apenas uma vez
TABELA_TRADUCAO = str.maketrans(
    '',
    '',
    string.punctuation
)

# =========================================
# PROCESSAMENTO DE TEXTO
# =========================================

def processar_texto(texto):

    texto = texto.lower()

    texto = texto.translate(
        TABELA_TRADUCAO
    )

    return texto.split()

# =========================================
# PROCESSA UM BLOCO
# =========================================

def processar_bloco(bloco):

    contador = Counter()

    total_palavras = 0

    for texto in bloco:

        palavras = processar_texto(str(texto))

        contador.update(palavras)

        total_palavras += len(palavras)

    return contador, total_palavras

# =========================================
# EXECUÇÃO COM THREADS
# =========================================

def contar_palavras_threads(df, num_threads):

    textos = df["text"]

    tamanho_bloco = len(textos) // num_threads

    blocos = []

    for i in range(num_threads):

        inicio = i * tamanho_bloco

        if i == num_threads - 1:
            fim = len(textos)
        else:
            fim = (i + 1) * tamanho_bloco

        blocos.append(
            textos.iloc[inicio:fim]
        )

    inicio_tempo = time.time()

    contador_total = Counter()

    total_palavras = 0

    with ThreadPoolExecutor(
        max_workers=num_threads
    ) as executor:

        resultados = executor.map(
            processar_bloco,
            blocos
        )

        for contador, quantidade in resultados:

            contador_total.update(contador)

            total_palavras += quantidade

    tempo_execucao = time.time() - inicio_tempo

    return tempo_execucao, total_palavras

# =========================================
# BENCHMARK
# =========================================

def benchmark_threads():

    print("Lendo base de dados...")

    df = pd.read_parquet("a.parquet")

    print(f"Total de artigos na base: {len(df):,}")

    df = df.head(LIMITE_ARTIGOS)

    print(f"Amostra utilizada: {len(df):,}")

    print("\n========== BENCHMARK ==========\n")

    resultados = []

    for n_threads in CONFIGURACOES:

        print(f"Executando com {n_threads} threads...")

        tempo, total = contar_palavras_threads(
            df,
            n_threads
        )

        resultados.append(
            (n_threads, tempo)
        )

        print(f"Tempo: {tempo:.2f} segundos")
        print(f"Total de palavras: {total}")

        print("-" * 60)

    print("\n========== RESUMO ==========\n")

    for threads, tempo in resultados:

        print(
            f"{threads} threads -> {tempo:.2f} segundos"
        )

# =========================================
# EXECUÇÃO
# =========================================

if __name__ == "__main__":
    benchmark_threads()