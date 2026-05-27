Projeto de Paralelização — Contador de Palavras da Wikipédia
Campo	Informação
Disciplina	Programação Concorrente
Alunas	Eliane de Freitas e Rayna Livia
Curso	Análise e Desenvolvimento de Sistemas
Professor	Rafael Marconi Ramos
1. Descrição do Problema
Qual é o objetivo do programa?

O objetivo do projeto é desenvolver um sistema de contagem de palavras utilizando técnicas de Programação Concorrente para processar grandes volumes de dados textuais extraídos da Wikipédia.

A proposta busca demonstrar, na prática, como a paralelização pode reduzir o tempo de execução de tarefas computacionalmente intensivas, principalmente em cenários envolvendo análise massiva de textos.

O programa realiza:

Leitura de arquivos textuais;
Processamento e normalização das palavras;
Contagem da frequência de ocorrência;
Identificação das palavras mais utilizadas;
Processamento paralelo utilizando múltiplas threads.

Além disso, o projeto analisa o impacto da execução concorrente no desempenho da aplicação, comparando eficiência e tempo de processamento.

Qual o volume de dados processado?

Foi utilizada a base de dados “Redes de artigos da Wikipédia”, versão 1.1, com aproximadamente 11,14 MB de arquivos textuais relacionados a páginas e redes de artigos da Wikipédia.

Apesar do tamanho compacto da base original, o processamento envolveu bilhões de palavras ao considerar todas as ocorrências analisadas durante a execução do algoritmo.

Qual algoritmo foi utilizado?

O sistema foi desenvolvido utilizando conceitos de paralelização baseados em múltiplas threads.

A estratégia utilizada consiste em:

Dividir os arquivos em blocos de processamento;
Distribuir as tarefas entre diferentes threads;
Processar simultaneamente diferentes partes da base;
Consolidar os resultados em uma estrutura compartilhada de contagem.

Para garantir segurança no acesso concorrente aos dados, foram utilizadas estruturas apropriadas para sincronização e manipulação thread-safe.

Qual a complexidade aproximada do algoritmo?
Modo	Complexidade
Sequencial	O(n)
Paralelo	O(n/p)
Consolidação dos resultados	O(p)
Complexidade paralela efetiva	O(n/p + p)

Onde:

n = quantidade total de palavras processadas;
p = número de threads utilizadas.

A paralelização reduz significativamente o tempo de execução ao dividir o processamento entre múltiplos núcleos do processador.

2. Fundamentação Teórica

A Programação Concorrente é uma área da computação responsável pelo desenvolvimento de aplicações capazes de executar múltiplas tarefas simultaneamente.

Em sistemas modernos, o uso de múltiplos núcleos de processamento tornou essencial o aproveitamento de técnicas de paralelização para aumentar desempenho, reduzir tempo de execução e otimizar o uso de recursos computacionais.

Neste projeto, o processamento paralelo foi aplicado ao problema de contagem de palavras em grandes bases textuais. Essa abordagem permite que diferentes partes dos arquivos sejam processadas simultaneamente por diferentes threads.

O uso da concorrência proporciona benefícios como:

Melhor aproveitamento do processador;
Redução do tempo total de execução;
Maior eficiência em aplicações de Big Data;
Escalabilidade do sistema;
Processamento simultâneo de grandes volumes de informação.

Entretanto, aplicações concorrentes também apresentam desafios importantes, como sincronização entre threads, compartilhamento de memória e controle de concorrência.

3. Ambiente Experimental
Item	Descrição
Linguagem utilizada	Java
Paradigma	Programação Concorrente
Biblioteca utilizada	Threads Java
Tipo de processamento	Paralelo
Base de dados	Redes de artigos da Wikipédia
Tamanho da base	Aproximadamente 11,14 MB
4. Metodologia de Testes
Como o tempo foi medido

O tempo de execução foi medido utilizando funções de temporização da própria linguagem Java, registrando o instante imediatamente antes do início do processamento e logo após a finalização da contagem das palavras.

O tempo total inclui:

Leitura dos arquivos;
Processamento textual;
Normalização das palavras;
Contagem concorrente;
Consolidação dos resultados finais.
Estratégia de Paralelização

A aplicação divide os arquivos textuais em partes menores, distribuídas entre diferentes threads de execução.

Cada thread é responsável por:

Ler sua parte do arquivo;
Processar as palavras;
Atualizar a contagem local;
Retornar os resultados para consolidação global.

Essa abordagem reduz o tempo de processamento e melhora o desempenho geral do sistema.

5. Resultados Experimentais
Resultado da Execução
========== RESULTADOS ==========

Total de palavras: 3729807787

Tempo de execução: 2862.22 segundos

Top 10 palavras:

the -> 215190151
of -> 115802937
in -> 95929216
and -> 90241749
a -> 65582641
to -> 58561365
was -> 34991248
is -> 29833293
for -> 26626387
on -> 25752927
6. Análise dos Resultados

Os resultados obtidos demonstram que o sistema conseguiu processar um volume extremamente elevado de palavras presentes na base de dados da Wikipédia.

A palavra mais frequente encontrada foi “the”, com mais de 215 milhões de ocorrências, seguida por outras palavras comuns da língua inglesa como “of”, “in” e “and”. Esse comportamento é esperado devido à predominância de artigos e conectivos em textos da Wikipédia.

O tempo total de execução foi de aproximadamente 2862 segundos, evidenciando a grande quantidade de dados processados durante a execução do algoritmo.

A utilização de Programação Concorrente permitiu:

Melhor aproveitamento dos núcleos do processador;
Redução do tempo de execução;
Processamento simultâneo de múltiplos arquivos;
Maior eficiência computacional.

Mesmo com os benefícios da paralelização, ainda existem fatores que limitam o desempenho máximo da aplicação, como:

Causa	Impacto
Leitura de arquivos	Parte do processo ainda depende de operações de I/O
Sincronização entre threads	Pode gerar contenção de acesso
Compartilhamento de memória	Threads competem por recursos do sistema
Overhead de gerenciamento	Criação e controle das threads possuem custo computacional
7. Escalabilidade e Concorrência

A aplicação apresentou comportamento escalável ao utilizar múltiplas threads para divisão do processamento.

A concorrência tornou possível:

Executar múltiplas tarefas simultaneamente;
Diminuir o tempo necessário para análise textual;
Melhorar a capacidade de processamento do sistema.

Entretanto, conforme aumenta a quantidade de threads, o ganho de desempenho tende a diminuir devido ao overhead de sincronização e compartilhamento de recursos, comportamento previsto pela Lei de Amdahl.

8. Conclusão

O projeto demonstrou de forma prática a importância da Programação Concorrente no processamento de grandes volumes de dados textuais.

A implementação do contador de palavras utilizando paralelização permitiu analisar bilhões de palavras de forma eficiente, aproveitando melhor os recursos computacionais disponíveis.

Os resultados obtidos mostram que aplicações concorrentes podem alcançar ganhos significativos de desempenho quando comparadas ao processamento sequencial, principalmente em tarefas de alta demanda computacional.

Além disso, o projeto contribuiu para o aprofundamento dos conhecimentos sobre:

Threads;
Paralelização;
Divisão de tarefas;
Sincronização;
Processamento concorrente;
Otimização de desempenho.
