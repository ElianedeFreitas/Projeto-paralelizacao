import pandas as pd
import time
import string

from collections import Counter
from concurrent.futures import ProcessPoolExecutor

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

def processar_bloco(bloco):

    contador = Counter()

    total_palavras = 0

    for texto in bloco:

        palavras = processar_texto(str(texto))

        contador.update(palavras)

        total_palavras += len(palavras)

    return contador, total_palavras

def executar_processos(df, num_processos):

    textos = df["text"].tolist()

    tamanho_bloco = len(textos) // num_processos

    blocos = []

    for i in range(num_processos):

        inicio = i * tamanho_bloco

        if i == num_processos - 1:
            fim = len(textos)
        else:
            fim = (i + 1) * tamanho_bloco

        blocos.append(
            textos[inicio:fim]
        )

    inicio_tempo = time.time()

    contador_total = Counter()

    total_palavras = 0

    with ProcessPoolExecutor(
        max_workers=num_processos
    ) as executor:

        resultados = executor.map(
            processar_bloco,
            blocos
        )

        for contador, qtd in resultados:

            contador_total.update(contador)

            total_palavras += qtd

    tempo = time.time() - inicio_tempo

    return (
        tempo,
        total_palavras,
        contador_total
    )

def benchmark_processos(arquivo):

    print("Lendo base de dados...")

    df = pd.read_parquet(arquivo)

    total_artigos = len(df)

    df = df.head(LIMITE_ARTIGOS)

    print(f"Total de artigos na base: {total_artigos:,}")
    print(f"Artigos processados: {len(df):,}")

    # 2 e 4 abaixo dos núcleos físicos (6)
    # 8 e 12 exploram as threads lógicas do hyperthreading
    configuracoes = [2, 4, 8, 12]

    resultados = []

    melhor_top10 = None

    print("\n========== BENCHMARK ==========\n")

    for processos in configuracoes:

        print(f"Executando com {processos} processos...")

        tempo, total, contador = executar_processos(
            df,
            processos
        )

        resultados.append(
            (processos, tempo)
        )

        if melhor_top10 is None:
            melhor_top10 = contador.most_common(10)

        print(f"Tempo de contagem: {tempo:.2f} segundos")
        print(f"Total de palavras: {total:,}")

        print("-" * 60)

    print("\n========== RESUMO ==========\n")

    # Tempo serial de referência (do benchmark anterior)
    tempo_serial = 989.68

    for processos, tempo in resultados:

        speedup = tempo_serial / tempo

        print(
            f"{processos} processos -> "
            f"{tempo:.2f} segundos  |  "
            f"Speedup: {speedup:.2f}x"
        )

    print("\n========== TOP 10 PALAVRAS ==========\n")

    for palavra, qtd in melhor_top10:

        print(f"{palavra} -> {qtd:,}")

# Obrigatório no Windows para uso de multiprocessing
if __name__ == "__main__":

    benchmark_processos("a.parquet")