# Projeto — Contador de Palavras da Wikipédia

| Informação | Detalhes |
|---|---|
| Disciplina | Programação Concorrente |
| Alunas | Eliane de Freitas e Rayna Livia |
| Curso | Análise e Desenvolvimento de Sistemas |
| Professor | Rafael Marconi Ramos |

---

# Introdução

O crescimento exponencial da quantidade de informações disponíveis na internet tornou necessária a criação de ferramentas capazes de processar e analisar grandes volumes de dados de forma eficiente. Nesse contexto, a Wikipédia representa uma das maiores fontes de conhecimento livre do mundo, contendo milhões de artigos sobre os mais diversos temas.

O presente projeto tem como objetivo desenvolver um sistema de contagem de palavras utilizando dados textuais da Wikipédia, aplicando conceitos de processamento de dados e programação concorrente. Além de servir como estudo prático de técnicas computacionais, a solução possui potencial para contribuir com diversas áreas da sociedade.

A análise da frequência de palavras em grandes bases textuais pode ser utilizada em pesquisas acadêmicas, sistemas de busca, processamento de linguagem natural, inteligência artificial, análise de tendências e desenvolvimento de ferramentas educacionais. Por meio desse tipo de processamento, é possível identificar padrões linguísticos, compreender melhor o comportamento da informação e auxiliar na organização de grandes repositórios de conhecimento.

Dessa forma, o projeto não apenas demonstra a aplicação de técnicas de computação em problemas reais, mas também evidencia como o tratamento eficiente de grandes volumes de dados pode contribuir para a produção, organização e disseminação do conhecimento em benefício da sociedade.

---

# Base de Dados

Foi utilizada a base “Wikipedia 20230701”, obtida através da plataforma Kaggle, contendo dados textuais extraídos da Wikipédia referentes à versão de julho de 2023.

A pasta completa da base possui aproximadamente 13 GB de dados, compostos por milhões de artigos da Wikipédia utilizados no processamento e análise das palavras durante a execução do sistema.

---

# Configuração do Ambiente

| Componente | Especificação |
|---|---|
| Processador | Ryzen 5 5600G |
| Número de Núcleos | 7 |
| Memória RAM | 32 GB |
| Linguagem Utilizada | Python |

---

# Funcionalidades

O programa realiza:

- Leitura dos arquivos;
- Processamento das palavras;
- Contagem de frequência;
- Exibição das palavras mais utilizadas.

---

# Tecnologias Utilizadas

| Tecnologia | Utilização |
|---|---|
| Python | Linguagem principal |
| Pandas | Manipulação de dados |
| PyArrow | Leitura de arquivos parquet |
| Wikipédia | Base de dados |
| Kaggle | Plataforma da base |

---

# Metodologia

O sistema realiza:

1. Leitura dos arquivos da Wikipédia;
2. Separação das palavras;
3. Contagem da frequência dos termos;
4. Organização dos resultados finais.

O tempo de execução foi medido considerando todo o processamento dos dados.

---

# Resultados Experimentais - Versão Serial

```text
========== RESULTADOS ==========

Total de palavras: 3.729.807.787

Tempo de execução: 2862.22 segundos

Top 10 palavras mais usadas:

the -> 215.190.151
of -> 115.802.937
in -> 95.929.216
and -> 90.241.749
a -> 65.582.641
to -> 58.561.365
was -> 34.991.248
is -> 29.833.293
for -> 26.626.387
on -> 25.752.927
```

---

# Implementação Paralela com Threads

Além da implementação serial, foi desenvolvida uma versão utilizando múltiplas threads com o objetivo de avaliar o impacto da concorrência no processamento dos dados.

Devido ao grande volume da base de dados completa (12.573.550 artigos), foi utilizada uma amostra de 1.000.000 de artigos para os experimentos paralelos, permitindo a execução de diversos testes em tempo viável.

A implementação paralela utilizou a biblioteca `concurrent.futures.ThreadPoolExecutor`, distribuindo os artigos entre diferentes threads para processamento simultâneo.

---

# Resultados Experimentais - Threads

### Base utilizada nos testes paralelos

| Métrica | Valor |
|----------|---------:|
| Total de artigos da base | 12.573.550 |
| Artigos utilizados nos testes | 1.000.000 |
| Total de palavras processadas | 525.310.204 |

### Tempo de execução por quantidade de threads

| Threads | Tempo (segundos) |
|----------|----------------:|
| 2 Threads | 623,30 |
| 4 Threads | 377,16 |
| 8 Threads | 383,65 |
| 12 Threads | 379,12 |

---

# Análise dos Resultados

Os resultados demonstram que o sistema conseguiu processar grandes volumes de dados textuais da Wikipédia com eficiência.

As palavras mais frequentes encontradas foram termos comuns da língua inglesa, como “the”, “of” e “in”, comportamento esperado em textos informativos.

O projeto mostrou a importância de técnicas de processamento textual para análise de grandes quantidades de informações.

Em relação à implementação paralela, observou-se que a utilização de múltiplas threads reduziu significativamente o tempo de execução quando comparada à execução com apenas 2 threads.

A melhor configuração encontrada foi a utilização de 4 threads, que apresentou o menor tempo de processamento entre os testes realizados.

Também foi observado que o aumento do número de threads para 8 e 12 não resultou em ganhos significativos de desempenho. Esse comportamento evidencia a existência de custos associados ao gerenciamento das threads e à disputa por recursos computacionais, limitando a escalabilidade da solução.

---

# Conclusão

O desenvolvimento do sistema permitiu aplicar conceitos de processamento textual, análise de dados e programação concorrente em um cenário real utilizando informações da Wikipédia.

Além disso, o projeto contribuiu para o entendimento prático de:

- Processamento de dados;
- Estruturação de informações;
- Análise textual;
- Otimização de desempenho;
- Programação concorrente com threads;
- Avaliação de escalabilidade.

Os experimentos demonstraram que a utilização de threads pode reduzir significativamente o tempo de processamento, porém o aumento do número de threads nem sempre resulta em ganhos proporcionais de desempenho.

O projeto demonstrou como técnicas computacionais podem ser utilizadas para analisar grandes volumes de dados de maneira eficiente, bem como a importância da escolha adequada da quantidade de threads para cada cenário de processamento.
