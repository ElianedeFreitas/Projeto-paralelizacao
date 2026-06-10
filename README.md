# Projeto — Contador de Palavras da Wikipédia

## Informações da Disciplina

| Informação | Detalhes |
|------------|----------|
| Disciplina | Programação Concorrente |
| Alunas | Eliane de Freitas e Rayna Livia |
| Curso | Análise e Desenvolvimento de Sistemas |
| Professor | Rafael Marconi Ramos |

---

# Introdução

O crescimento exponencial da quantidade de informações disponíveis na internet tornou necessária a criação de ferramentas capazes de processar e analisar grandes volumes de dados de forma eficiente. Nesse contexto, a Wikipédia representa uma das maiores fontes de conhecimento livre do mundo, contendo milhões de artigos sobre os mais diversos temas.

O presente projeto tem como objetivo desenvolver um sistema de contagem de palavras utilizando dados textuais da Wikipédia, aplicando conceitos de processamento de dados e programação paralela.

A análise da frequência de palavras em grandes bases textuais pode auxiliar pesquisas acadêmicas, sistemas de busca, aplicações de inteligência artificial, processamento de linguagem natural e ferramentas educacionais. Dessa forma, o projeto demonstra como técnicas computacionais podem contribuir para a organização e análise de grandes volumes de informação.

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
|----------|-------:|
| Artigos processados | 1.000.000 |
| Total de palavras | 525.310.204 |
| Tempo de execução | 349,22 s |


---

## Versão Paralela

### Resultados Obtidos

| Processos | Tempo (s) |
|-----------|----------:|
| 2 | 216,98 |
| 4 | 119,25 |
| 8 | 79,97 |
| 12 | 69,86 |

---

# Cálculo do Speedup

O speedup foi calculado utilizando a seguinte fórmula:

```text
Speedup = Tempo Serial / Tempo Paralelo
```

Onde:

- Tempo Serial = 349,22 segundos
- Tempo Paralelo = tempo obtido em cada configuração

---

# Estatísticas de Desempenho

| Configuração | Tempo (s) | Speedup |
|--------------|----------:|---------:|
| Serial | 349,22 | 1,00x |
| 2 Processos | 216,98 | 1,61x |
| 4 Processos | 119,25 | 2,93x |
| 8 Processos | 79,97 | 4,37x |
| 12 Processos | 69,86 | 5,00x |

### Redução do Tempo de Execução

| Configuração | Redução |
|--------------|---------:|
| 2 Processos | 37,87% |
| 4 Processos | 65,85% |
| 8 Processos | 77,10% |
| 12 Processos | 79,99% |

---

### Top 10 Palavras

| Palavra | Ocorrências |
|----------|-----------:|
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

A execução serial levou aproximadamente **349 segundos** para processar mais de **525 milhões de palavras**. Já a versão paralela com **12 processos** concluiu a mesma tarefa em aproximadamente **70 segundos**.

Observou-se uma redução progressiva do tempo de execução conforme a quantidade de processos aumentava, evidenciando o aproveitamento dos múltiplos núcleos disponíveis no processador.

A melhor configuração encontrada foi a execução com **12 processos**, que apresentou o menor tempo de execução e o maior speedup.

Os resultados também mostram que o ganho de desempenho não cresce de forma perfeitamente linear, devido aos custos de sincronização, gerenciamento dos processos e compartilhamento de recursos do sistema operacional.

---

# Conclusão

O desenvolvimento do sistema permitiu aplicar conceitos de processamento textual, análise de dados e programação paralela em um cenário real utilizando informações da Wikipédia.

Durante os experimentos foram processados mais de **525 milhões de palavras**, demonstrando a capacidade da aplicação de lidar com grandes volumes de dados.

Os resultados evidenciaram os benefícios da paralelização, reduzindo o tempo de execução de **349,22 segundos** para **69,86 segundos**, alcançando um speedup de aproximadamente **5 vezes** em relação à execução serial.

O projeto contribuiu para o entendimento prático de:

- Processamento de dados;
- Estruturação de informações;
- Análise textual;
- Programação paralela;
- Medição de desempenho;
- Cálculo de speedup;
- Avaliação de escalabilidade.

Dessa forma, foi possível demonstrar na prática como técnicas de paralelização podem aumentar significativamente a eficiência computacional no processamento de grandes bases de dados.
