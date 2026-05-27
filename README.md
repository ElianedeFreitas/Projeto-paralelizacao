Projeto de Paralelização — Contador de Palavras da Wikipédia
Campo	Informação
Disciplina	Programação Concorrente
Alunas	Eliane de Freitas e Rayna Livia
Curso	Análise e Desenvolvimento de Sistemas
Professor	Rafael Marconi Ramos
1. Descrição do Problema

O objetivo do projeto é desenvolver um sistema de contagem de palavras utilizando Programação Concorrente para processar grandes volumes de dados textuais extraídos da Wikipédia.

O programa realiza:

Leitura dos arquivos;
Processamento das palavras;
Contagem de frequência;
Paralelização utilizando múltiplas threads.

A proposta busca demonstrar como o uso de concorrência melhora o desempenho e reduz o tempo de processamento em aplicações que trabalham com grande quantidade de dados.

2. Base de Dados

Foi utilizada a base “Redes de artigos da Wikipédia”, versão 1.1, contendo aproximadamente 11,14 MB de dados textuais relacionados a páginas da Wikipédia.

O processamento envolveu bilhões de palavras analisadas durante a execução do sistema.

3. Algoritmo Utilizado

O sistema utiliza processamento paralelo com múltiplas threads.

A estratégia consiste em:

Dividir os arquivos em partes menores;
Distribuir as tarefas entre diferentes threads;
Processar simultaneamente os dados;
Consolidar os resultados finais.

A complexidade aproximada do algoritmo é:

Modo	Complexidade
Sequencial	O(n)
Paralelo	O(n/p)
Consolidação	O(p)

Onde:

n = quantidade de palavras;
p = número de threads.
4. Ambiente Experimental
Item	Descrição
Linguagem	Java
Paradigma	Programação Concorrente
Biblioteca	Threads Java
Base de dados	Wikipédia
Tipo de processamento	Paralelo
5. Metodologia de Testes

O tempo de execução foi medido antes e após o processamento completo dos arquivos, incluindo:

Leitura dos dados;
Processamento textual;
Contagem das palavras;
Consolidação dos resultados.

Cada thread ficou responsável por processar uma parte da base de dados simultaneamente.

6. Resultados Experimentais
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
7. Análise dos Resultados

Os resultados mostram que o sistema conseguiu processar bilhões de palavras da base da Wikipédia utilizando Programação Concorrente.

As palavras mais frequentes encontradas foram termos comuns da língua inglesa, como “the”, “of” e “in”, comportamento esperado em textos da Wikipédia.

A paralelização permitiu:

Melhor aproveitamento do processador;
Redução do tempo de execução;
Processamento simultâneo de múltiplos dados.

Mesmo assim, fatores como leitura de arquivos, sincronização entre threads e compartilhamento de memória ainda influenciam no desempenho final do sistema.

8. Conclusão

O projeto demonstrou a importância da Programação Concorrente no processamento de grandes volumes de dados.

A utilização de múltiplas threads tornou o processamento mais eficiente, reduzindo o tempo necessário para análise textual e melhorando o desempenho da aplicação.

Além disso, o projeto contribuiu para a compreensão prática de conceitos como:

Threads;
Paralelização;
Sincronização;
Processamento concorrente;
Otimização de desempenho.

O desenvolvimento do sistema mostrou como técnicas de concorrência podem ser aplicadas em cenários reais envolvendo processamento massivo de informações.
Sincronização;
Processamento concorrente;
Otimização de desempenho.
