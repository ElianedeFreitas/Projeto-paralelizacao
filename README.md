# Projeto — Contador de Palavras 

## Informações da Disciplina

| Informação | Detalhes |
| ---------- | -------- |
| Disciplina | Programação Concorrente |
| Alunas | Eliane de Freitas e Rayna Livia |
| Curso | Análise e Desenvolvimento de Sistemas |
| Professor | Rafael Marconi Ramos |

---

# Introdução

O crescimento exponencial da quantidade de informações disponíveis na internet tornou necessária a criação de ferramentas capazes de processar e analisar grandes volumes de dados de forma eficiente. Nesse contexto, a Wikipédia representa uma das maiores fontes de conhecimento livre do mundo, contendo milhões de artigos sobre os mais diversos temas.

O presente projeto tem como objetivo desenvolver um sistema de contagem de palavras utilizando dados textuais da Wikipédia, aplicando conceitos de processamento de dados e programação paralela.

A análise da frequência de palavras em grandes bases textuais possui diversas aplicações práticas e científicas. Essa técnica é utilizada por motores de busca, como o Google, para identificar quais páginas são mais relevantes para uma pesquisa. Também é fundamental em áreas de Inteligência Artificial e Processamento de Linguagem Natural, onde a análise de bilhões de palavras permite identificar termos importantes, construir vocabulários, treinar modelos de IA e aprimorar tradutores automáticos e assistentes virtuais. Além disso, a contagem de palavras auxilia pesquisadores na análise da evolução da linguagem, das mudanças culturais, dos temas mais estudados ao longo do tempo e da produção científica em diferentes áreas do conhecimento. Dessa forma, o projeto demonstra como técnicas computacionais podem contribuir para a organização, análise e extração de informações relevantes a partir de grandes volumes de dados textuais.
---

# Base de Dados

Foi utilizada a base **Wikipedia 20230701**, obtida através da plataforma Kaggle, contendo artigos da Wikipédia referentes à versão de julho de 2023.

A base completa possui aproximadamente **13 GB de dados**, distribuídos em **12.573.550 artigos**.

Para os testes de desempenho foi utilizada uma amostra de **1.000.000 de artigos**, totalizando **525.310.204 palavras processadas**.

---

# Configuração do Ambiente

| Componente | Especificação |
|------------|--------------|
| Processador | Ryzen 5 5600G |
| Núcleos | 6 núcleos físicos / 12 threads |
| Memória RAM | 32 GB |
| Linguagem Utilizada | Python 3.13 |

---

# Tecnologias Utilizadas

| Tecnologia | Utilização |
|------------|------------|
| Python | Linguagem principal |
| Pandas | Manipulação dos dados |
| PyArrow | Leitura dos arquivos Parquet |
| Multiprocessing | Paralelização |
| Wikipédia | Base de dados |
| Kaggle | Plataforma da base |

---

# Metodologia

O sistema realiza as seguintes etapas:

1. Leitura dos artigos da Wikipédia;
2. Conversão do texto para minúsculas;
3. Remoção de pontuações;
4. Separação das palavras;
5. Contagem da frequência dos termos;
6. Organização dos resultados;
7. Exibição das palavras mais frequentes.

Foram desenvolvidas duas versões da aplicação:

- Versão Serial;
- Versão Paralela utilizando múltiplos processos.

---

# Resultados Experimentais

## Versão Serial

### Dados Processados

| Métrica | Valor |
|----------|----------|
| Artigos processados | 1.000.000 |
| Total de palavras | 525.310.204 |
| Tempo de execução | 349,22 s |

---

## Versão Paralela

### Resultados Obtidos

| Processos | Tempo (s) |
|------------|-----------|
| 2 | 216,98 |
| 4 | 119,25 |
| 8 | 79,97 |
| 12 | 69,86 |

---

# Cálculo do Speedup

O speedup foi calculado utilizando a fórmula:

**Speedup = Tempo Serial / Tempo Paralelo**

Onde:

- Tempo Serial = 349,22 segundos
- Tempo Paralelo = tempo obtido em cada configuração

---

# Estatísticas de Desempenho

| Configuração | Tempo (s) | Speedup |
|------------|-----------|---------|
| Serial | 349,22 | 1,00x |
| 2 Processos | 216,98 | 1,61x |
| 4 Processos | 119,25 | 2,93x |
| 8 Processos | 79,97 | 4,37x |
| 12 Processos | 69,86 | 5,00x |

---

## Redução do Tempo de Execução

| Configuração | Redução |
|------------|---------|
| 2 Processos | 37,87% |
| 4 Processos | 65,85% |
| 8 Processos | 77,10% |
| 12 Processos | 79,99% |

---

## Eficiência Obtida

A eficiência foi calculada utilizando a fórmula:

**Eficiência = Speedup / Número de Processos**

| Configuração | Speedup | Eficiência |
|------------|----------|------------|
| Serial | 1,00x | 100,0% |
| 2 Processos | 1,61x | 80,5% |
| 4 Processos | 2,93x | 73,3% |
| 8 Processos | 4,37x | 54,6% |
| 12 Processos | 5,00x | 41,7% |

---

# Gráfico de Speedup

<img src="https://github.com/user-attachments/assets/d0f6ed28-8429-4642-b81b-1fdf3248da90" width="700">


---

# Gráfico de Eficiência

<img src="https://github.com/user-attachments/assets/9e7b7183-ebc3-4aca-a7cb-63c467343218" width="700">

---

# Top 10 Palavras

| Palavra | Ocorrências |
|----------|-------------|
| the | 32.040.567 |
| of | 17.093.205 |
| in | 14.274.333 |
| and | 13.486.227 |
| a | 9.334.795 |
| to | 8.813.944 |
| was | 5.217.657 |
| is | 4.017.112 |
| for | 3.887.672 |
| on | 3.804.643 |

---

# Análise dos Resultados

Os resultados demonstram que a paralelização proporcionou uma redução significativa do tempo de processamento quando comparada à versão serial.

A execução serial levou aproximadamente **349,22 segundos** para processar mais de **525 milhões de palavras**. Já a versão paralela com **12 processos** concluiu a mesma tarefa em **69,86 segundos**, alcançando um speedup de aproximadamente **5 vezes**.

Entretanto, os resultados ficaram abaixo do desempenho ideal esperado para uma paralelização perfeita. Esse comportamento pode ser explicado por dois fatores principais.

## Motivo 1 — Overhead do Multiprocessing no Windows

O primeiro fator está relacionado aos custos inerentes ao módulo **Multiprocessing** no sistema operacional Windows.

Durante a execução paralela, parte do tempo é consumida por atividades que não realizam processamento útil diretamente, como:

- Criação dos processos utilizando o método *spawn*;
- Recarregamento do interpretador Python em cada processo;
- Serialização (*pickle*) dos dados enviados aos processos;
- Desserialização dos resultados recebidos;
- Combinação dos contadores de palavras ao final da execução.

Esses custos representam uma parcela significativa do tempo total quando poucos processos são utilizados.


---

## Motivo 2 — Lei de Amdahl

O segundo fator é explicado pela **Lei de Amdahl**, que estabelece que o ganho máximo de paralelização é limitado pelas partes do programa que não podem ser executadas em paralelo.

No projeto, as seguintes etapas permanecem sequenciais:

- Leitura do arquivo Parquet;
- Distribuição dos blocos de dados;
- Serialização e transferência de informações;
- Agregação dos resultados finais.

À medida que mais processos são adicionados, essas partes passam a representar uma parcela cada vez maior do tempo total de execução.


---

## Comparação entre Speedup Obtido e Speedup Ideal

| Processos | Speedup Obtido | Speedup Ideal |
|-----------|---------------|---------------|
| 2 | 1,61x | 2,00x |
| 4 | 2,93x | 4,00x |
| 8 | 4,37x | 8,00x |
| 12 | 5,00x | 12,00x |

Observa-se que a distância entre o speedup obtido e o speedup ideal aumenta conforme o número de processos cresce, comportamento previsto pela Lei de Amdahl.

Da mesma forma, a eficiência diminui progressivamente:

| Configuração | Eficiência |
|-------------|------------|
| 2 Processos | 80,5% |
| 4 Processos | 73,3% |
| 8 Processos | 54,6% |
| 12 Processos | 41,7% |

A queda da eficiência mostra que cada novo processo contribui menos para o ganho total de desempenho. Isso ocorre porque uma parcela crescente do tempo passa a ser consumida por comunicação, sincronização e gerenciamento dos processos.

### Observação dos Gráficos

Os gráficos tornam visíveis dois comportamentos importantes:

1. **Speedup Obtido vs Speedup Ideal:** a curva do speedup real permanece abaixo da curva ideal, evidenciando as limitações impostas pela Lei de Amdahl.

2. **Eficiência Decrescente:** a eficiência diminui conforme o número de processos aumenta, indicando que cada processo adicional possui um aproveitamento menor do que os anteriores.

Esses resultados demonstram que a paralelização melhora significativamente o desempenho, porém seus ganhos não crescem indefinidamente.

---

# Conclusão

O desenvolvimento do sistema permitiu aplicar conceitos de processamento textual, análise de dados e programação paralela em um cenário real utilizando informações da Wikipédia.

Durante os experimentos foram processados mais de **525 milhões de palavras**, demonstrando a capacidade da aplicação de lidar com grandes volumes de dados.

Os resultados evidenciaram os benefícios da paralelização, reduzindo o tempo de execução de **349,22 segundos para 69,86 segundos**, alcançando um speedup de aproximadamente **5 vezes** em relação à execução serial.

O projeto contribuiu para o entendimento prático de:

- Processamento de dados;
- Estruturação de informações;
- Análise textual;
- Programação paralela;
- Medição de desempenho;
- Cálculo de speedup;
- Cálculo de eficiência;
- Avaliação de escalabilidade;
- Lei de Amdahl aplicada na prática.

Dessa forma, foi possível demonstrar como técnicas de paralelização podem aumentar significativamente a eficiência computacional no processamento de grandes bases de dados, ao mesmo tempo em que evidenciam os limites práticos impostos pelos custos de comunicação entre processos e pelas partes não paralelizáveis do algoritmo.
