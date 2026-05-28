# Arquitetura da evolução N2

## Visão geral

A aplicação foi organizada em camadas para separar responsabilidades:

```text
Interface Web
    ↓
Rotas FastAPI
    ↓
SearchService
    ↓
SearchStrategy
    ↓
Algoritmos concretos
```

## Camadas

### Domain

Contém os contratos e estruturas centrais:

- `SearchStrategy`: interface base para os algoritmos.
- `SearchResult`: retorno padronizado das execuções.

### Strategies

Contém os algoritmos:

- `NaiveSearch`
- `RabinKarpSearch`
- `KMPSearch`
- `BoyerMooreSearch`

### Services

A camada `SearchService` escolhe a estratégia correta, executa a busca, registra logs, cria traces, envia métricas e salva dados para o dashboard.

### Observability

Contém a configuração de logs e OpenTelemetry.

Cada execução registra:

- Trace: `search.execution`
- Métrica: `search_execution_total`
- Métrica: `search_execution_time_ms`
- Métrica: `search_comparisons_total`
- Métrica: `search_occurrences_total`

### Static

Contém a interface web e o dashboard interno.

## Justificativa

Essa organização permite evoluir a aplicação com menor acoplamento. Novos algoritmos podem ser adicionados criando uma nova classe que implemente `SearchStrategy`, sem alterar a interface ou a API principal.
