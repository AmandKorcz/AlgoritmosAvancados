# Roteiro sugerido para vídeo de apresentação

## 1. Abertura

Apresentar o objetivo da N2: evoluir a aplicação anterior de comparação de algoritmos de busca em strings, agora com foco em qualidade de código, padrão Strategy, observabilidade, OpenTelemetry, dashboard e análise com arquivos reais.

## 2. Relembrar a primeira entrega

Explicar rapidamente que a primeira versão já executava os algoritmos Naive, Rabin-Karp, KMP e Boyer-Moore, permitindo medir tempo, comparações e visualizar o passo a passo.

## 3. Mostrar a nova arquitetura

Apresentar a estrutura de pastas:

- `domain`: contratos e estruturas de retorno.
- `strategies`: algoritmos concretos.
- `services`: orquestra a execução.
- `routes`: endpoints da API.
- `observability`: logs, métricas e traces.
- `static`: interface e dashboard.

## 4. Explicar o Strategy

Mostrar a interface `SearchStrategy` e explicar que cada algoritmo implementa o mesmo contrato. Isso permite trocar o algoritmo em tempo de execução sem alterar a camada principal da aplicação.

## 5. Explicar o SearchResult

Mostrar que todos os algoritmos retornam os mesmos campos: algoritmo, ocorrências, comparações, tempo, tamanho do texto, tamanho do padrão, complexidade teórica, dados auxiliares e logs.

## 6. Demonstrar a aplicação

Executar uma busca com um arquivo `.txt`, depois executar o passo a passo e, por fim, usar a opção de comparar todos.

## 7. Mostrar observabilidade

Mostrar no console os logs de início e fim da execução. Depois mostrar os spans e métricas exportados pelo OpenTelemetry.

## 8. Mostrar dashboard

Mostrar o dashboard com número de execuções, tempo médio por algoritmo e comparações médias.

## 9. Análise final

Comentar que, na prática, o Naive tende a fazer mais comparações, enquanto KMP e Boyer-Moore tendem a reduzir comparações por usarem estruturas auxiliares. Rabin-Karp pode ter bom desempenho médio por usar hash.

## 10. Fechamento

Concluir que a N2 evoluiu a aplicação tecnicamente, deixando o projeto mais organizado, monitorável e adequado para análise comparativa com dados reais.
