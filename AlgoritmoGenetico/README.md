# Algoritmo Genético - Problema da Mochila

Este projeto foi desenvolvido como atividade acadêmica com o objetivo de resolver o problema clássico da mochila, conhecido como **Knapsack Problem**, utilizando um **algoritmo genético** com interface visual em React.

A aplicação permite simular a escolha de itens de sobrevivência para uma mochila com capacidade máxima de **30 kg**, buscando a melhor combinação possível entre peso e pontuação.

---

## 1. Descrição do problema

O cenário proposto considera uma pessoa isolada na natureza selvagem, que pode carregar apenas uma mochila com capacidade máxima de **30 kg**.

Cada item disponível possui:

- um peso;
- uma pontuação de sobrevivência.

O objetivo da aplicação é encontrar a melhor combinação possível de itens, maximizando a pontuação total sem ultrapassar o limite de peso da mochila.

---

## 2. Itens disponíveis

| Item           | Peso  | Pontuação |
|----------------|-------|-----------|
| Saco de dormir | 15 kg | 15        |
| Corda          | 3  kg | 7         |
| Canivete       | 2  kg | 10        |
| Tocha          | 5  kg | 5         |
| Garrafa        | 9  kg | 8         |
| Comida         | 20 kg | 17        |

---

## 3. Tecnologias utilizadas

- React
- Vite
- JavaScript
- CSS
- Recharts

---

## 4. Como executar o projeto

### 4.1. Baixar ou descompactar o projeto

Após baixar ou descompactar o projeto, acesse a pasta pelo terminal:

```bash
cd knapsack-genetic-algorithm
```

### 4.2. Instalar as dependências

```bash
npm install
```

### 4.3. Executar a aplicação

```bash
npm run dev
```

Depois, acesse no navegador o endereço exibido no terminal.
A aplicação estará disponível em:

```bash
http://localhost:5173/
```

---

## 5. Estrutura do projeto

```txt
src/
├── components/
│   ├── AlgorithmConfig.jsx
│   ├── FitnessChart.jsx
│   ├── ItemsTable.jsx
│   └── ResultCard.jsx
│
├── data/
│   └── items.js
│
├── genetic/
│   └── geneticAlgorithm.js
│
├── App.jsx
├── main.jsx
└── styles.css
```

---

## 6. Funcionamento da aplicação

A aplicação possui uma interface visual que permite:

- visualizar os itens disponíveis;
- consultar peso e pontuação de cada item;
- configurar o tamanho da população, número de gerações, taxa de mutação;
- executar o algoritmo genético;
- visualizar o melhor cromossomo encontrado, o peso total da mochila, a pontuação total e os itens selecionados
- acompanhar a evolução do fitness por geração em um gráfico.

---

## 7. Representação genética

Cada solução é representada por um cromossomo binário.

Exemplo:

```txt
101010
```

Cada posição do cromossomo representa um item da lista:

| Gene | Item           |
|------|----------------|
| 1    | Saco de dormir |
| 0    | Corda          |
| 1    | Canivete       |
| 0    | Tocha          |
| 1    | Garrafa        |
| 0    | Comida         |

Nesse exemplo, os itens selecionados seriam:

- Saco de dormir;
- Canivete;
- Garrafa.

O valor `1` indica que o item será levado na mochila, enquanto o valor `0` indica que o item não será levado.

---

## 8. Funcionamento do algoritmo genético

O algoritmo genético implementado segue as seguintes etapas:

1. Criação da população inicial;
2. Cálculo da função de fitness;
3. Seleção dos indivíduos;
4. Crossover;
5. Mutação;
6. Elitismo;
7. Evolução por gerações;
8. Retorno da melhor solução encontrada.

---

## 8.1. População inicial

A população inicial é criada de forma aleatória.

Cada indivíduo da população representa uma possível solução para o problema da mochila. Como existem seis itens disponíveis, cada cromossomo possui seis genes.

Exemplo de população inicial:

```txt
101010
011001
111000
000111
```

Cada cromossomo representa uma combinação diferente de itens que podem ou não ser levados na mochila.

---

## 8.2. Função de fitness

A função de fitness avalia a qualidade de cada solução.

O objetivo é maximizar a pontuação total dos itens selecionados sem ultrapassar o limite de peso da mochila.

A regra utilizada foi:

- se o peso total for menor ou igual a **30 kg**, o fitness será igual à pontuação total;
- se o peso total ultrapassar **30 kg**, o fitness será **0**.

Dessa forma, soluções inválidas são penalizadas e deixam de ser favorecidas pelo algoritmo.

Exemplo de solução válida:

```txt
Cromossomo: 011101
Peso total: 30 kg
Pontuação total: 39
Fitness: 39
```

Exemplo de solução inválida:

```txt
Cromossomo: 111111
Peso total: 54 kg
Pontuação total: 62
Fitness: 0
```

Mesmo possuindo uma pontuação alta, a segunda solução ultrapassa o limite de peso permitido, por isso recebe fitness igual a zero.

---

## 8.3. Seleção

A seleção é feita por torneio.

Nesse método, alguns indivíduos são escolhidos aleatoriamente da população, e o melhor entre eles é selecionado como pai para gerar novos indivíduos.

Esse processo favorece indivíduos com maior fitness, mas ainda mantém diversidade na população, pois a seleção possui um componente aleatório.

Exemplo simplificado:

```txt
Indivíduo A - Fitness 20
Indivíduo B - Fitness 39
Indivíduo C - Fitness 17
```

Nesse torneio, o indivíduo B seria selecionado por possuir o maior fitness.

---

## 8.4. Crossover

O crossover utilizado é o de ponto único.

Nesse processo, dois pais são combinados para gerar um novo filho. Uma parte do cromossomo vem do primeiro pai e a outra parte vem do segundo pai.

Exemplo:

```txt
Pai 1: 101 | 010
Pai 2: 011 | 101
Filho: 101 | 101
```

O ponto de corte é escolhido aleatoriamente, permitindo a criação de novas combinações de itens.

---

## 8.5. Mutação

A mutação altera aleatoriamente alguns genes do cromossomo.

A mutação é importante porque permite gerar novas possibilidades que talvez não existissem na população inicial.

Exemplo:

```txt
Antes: 101010
Depois: 101110
```

Nesse exemplo, um gene foi alterado de `0` para `1`.

A taxa de mutação pode ser configurada na interface da aplicação.

Exemplos:

```txt
0.01 = 1%
0.05 = 5%
0.10 = 10%
```

---

## 8.6. Elitismo

O algoritmo utiliza elitismo.

Isso significa que o melhor indivíduo de cada geração é mantido automaticamente na próxima geração.

O elitismo evita que a melhor solução encontrada seja perdida durante os processos de crossover e mutação.

---

## 8.7. Evolução por gerações

O processo de avaliação, seleção, crossover, mutação e elitismo é repetido durante o número de gerações configurado pelo usuário.

A cada geração, o algoritmo tenta melhorar a qualidade das soluções.

Ao final da execução, a aplicação retorna a melhor solução encontrada.

---

## 9. Resultado apresentado

Após a execução do algoritmo, a aplicação apresenta:

- melhor cromossomo encontrado;
- peso total;
- pontuação total;
- fitness;
- itens selecionados;
- gráfico da evolução do fitness por geração.

---

## 10. Exemplo de resultado

Um possível resultado encontrado pelo algoritmo é:

```txt
Cromossomo: 011101
Peso total: 30 kg
Pontuação total: 39
Fitness: 39
```

Esse cromossomo representa os seguintes itens:

| Gene | Item           | Peso  | Pontuação |
|------|----------------|-------|-----------|
| 0    | Saco de dormir | 15 kg | 15        |
| 1    | Corda          | 3  kg | 7         |
| 1    | Canivete       | 2  kg | 10        |
| 1    | Tocha          | 5  kg | 5         |
| 0    | Garrafa        | 9  kg | 8         |
| 1    | Comida         | 20 kg | 17        |

Itens selecionados:

| Item     | Peso  | Pontuação |
|----------|-------|-----------|
| Corda    | 3  kg | 7         |
| Canivete | 2  kg | 10        |
| Tocha    | 5  kg | 5         |
| Comida   | 20 kg | 17        |

Total:

```txt
Peso: 30 kg
Pontuação: 39
```

Como o peso total respeita o limite de 30 kg, essa é uma solução válida.