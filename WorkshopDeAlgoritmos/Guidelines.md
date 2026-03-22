# Workshop de Algoritmos: Do Papel ao Código

Esta é uma atividade prática com o objetivo de reforçar habilidades fundamentais de desenvolvimento de algoritmos. 
A proposta é uma lista de exercícios com complexidade incremental, resolvida em duplas, estimulando raciocínio lógico,
clareza na descrição de algoritmos e capacidade de revisão crítica. Os exercícios devem ser desenvolvidos no papel,
utilizando a linguagem de programação que a dupla preferir (Python, C, Java, JavaScript ou pseudocódigo estruturado).
Os problemas são apresentados em contextos lúdicos, evitando inicialmente discussões formais de análise de
complexidade. A intenção é fortalecer a intuição algorítmica, que posteriormente será formalizada ao longo da disciplina.

### A atividade será organizada em 4 rodadas, cada uma com:
    • 30 minutos de desenvolvimento
    • 5 minutos de revisão por outra dupla

Durante a revisão, os alunos devem atuar como um “compilador humano”, verificando se o algoritmo é claro, correto e
executável.

### A revisão deve observar:
    • Sintaxe: o código é legível? Há erros estruturais evidentes?
    • Lógica: o algoritmo resolve o problema proposto?
    • Clareza: outra pessoa conseguiria executar os passos sem se confundir?
    • Erros comuns: loops infinitos, índices incorretos ou casos não tratados.

## 1. O Caos da Biblioteca 
Uma biblioteca recebeu vários livros numerados, mas alguém os devolveu completamente fora de ordem na estante. 

**Resumo Desafio:** Escreva um algoritmo que receba uma lista de números representando livros fora de ordem e reorganize a lista 
em ordem crescente. Você só pode comparar livros adjacentes e decidir se troca ou não a posição deles. 

**Objetivo conceitual:** Introduzir o raciocínio de algoritmos de ordenação simples baseados em comparações sucessivas (intuição para Bubble Sort). 

**Estratégia de review:** A dupla revisora deve verificar se o algoritmo realmente percorre toda a lista e se existe uma condição clara para 
parar quando a lista estiver ordenada.

## 2. O Porteiro da Festa
Um porteiro possui uma lista com os nomes de todos os convidados autorizados a entrar em uma festa.

**Resumo Desafio:** Escreva um algoritmo que receba uma lista de nomes e verifique se um determinado nome está presente. 

**Objetivo conceitual:** Introduzir a busca sequencial (busca linear).

**Estratégia de review:** Verificar se o algoritmo percorre corretamente todos os elementos e se trata corretamente o caso em que o nome não existe na lista. 

## 3. O Dia Mais Quente
Um meteorologista registrou várias temperaturas ao longo do dia. 

**Resumo Desafio:** Escreva um algoritmo que percorra a lista de temperaturas e determine qual foi a maior temperatura registrada.

**Objetivo conceitual:** Introduzir o padrão de algoritmo que percorre uma coleção mantendo um valor máximo. 

**Estratégia de review:** Verificar se o algoritmo inicializa corretamente o valor máximo e se compara todos os elementos da lista. 

## 4. A Corrida de Cavalos
Uma corrida registrou os tempos de chegada de vários cavalos. 

**Resumo Desafio:** Escreva um algoritmo que determine os dois melhores tempos (primeiro e segundo lugar) a partir de uma lista de valores. 

**Objetivo conceitual:** Trabalhar a manutenção simultânea de dois valores máximos ou mínimos. 

**Estratégia de review:** Verificar se o algoritmo funciona corretamente quando o maior valor aparece no final da lista. 

## 5. O Arquivo Corrompido
Uma empresa possui uma lista de usuários organizada em ordem alfabética.

**Resumo Desafio:** Escreva um algoritmo que encontre um nome específico explorando o fato de que a lista já está ordenada. 

**Objetivo conceitual:** Introduzir o conceito de divisão do problema pela metade (busca binária). 

**Estratégia de review:** Verificar se o cálculo do elemento central está correto e se o algoritmo trata o caso em que o elemento não existe.

## 6. O Jogo da Adivinhação
Um jogador pensa em um número entre 1 e 100. Outro jogador só pode perguntar se o número é maior ou menor do que um valor sugerido. 

**Resumo Desafio:** Descreva a estratégia que permite descobrir o número  em no máximo 7 tentativas. 

**Objetivo conceitual:** Aplicação da estratégia de busca binária em um espaço numérico. 

**Estratégia de review:** Verificar se a estratégia sempre reduz o espaço de busca pela metade. 

## 7. O Pátio de Containers
Em um porto existem containers com pesos diferentes. 

**Resumo Desafio:**
Escreva um algoritmo que identifique os dois containers mais pesados usando o menor número possível de comparações. 

**Objetivo conceitual:**
Introduzir a ideia de comparação eficiente e raciocínio similar a árvores de torneio. 

**Estratégia de review:**
Contar quantas comparações são feitas e verificar se o algoritmo funciona independentemente da posição dos maiores valores.

## 8. O Detector de Duplicatas
Uma base de dados possui milhares de identificadores de usuários. 

**Resumo Desafio:**
Escreva um algoritmo que verifique se existe algum valor repetido na lista. 

**Objetivo conceitual:**
Introduzir o problema de detecção de duplicatas e raciocínio sobre comparações entre elementos. 

**Estratégia de review:** 
Verificar se o algoritmo realmente compara todos os pares necessários ou se pode deixar passar duplicatas. 

## 9. A Escada de Cores
Um artista possui lápis de diferentes tons de azul, mas eles estão misturados. 

**Resumo Desafio:**
Descreva um algoritmo que organize os lápis do tom mais claro ao mais escuro, podendo comparar apenas dois lápis por vez. 

**Objetivo conceitual:**
Reforçar raciocínio de ordenação incremental e comparações sucessivas. 

**Estratégia de review:**
Verificar se o algoritmo garante que todos os elementos acabam na posição correta. 

# 10. A Torre de Panquecas
Uma pilha de panquecas possui tamanhos diferentes. A única operação permitida é inserir uma espátula em um ponto da pilha e inverter todas as panquecas acima dela. 

**Resumo Desafio:**
Descreva um algoritmo que ordene a pilha da maior panqueca (embaixo) para a menor (no topo). 

**Objetivo conceitual:**
Introduzir algoritmos com restrições de operação (Pancake Sorting). 

**Estratégia de review:**
Verificar se a estratégia de inversão realmente posiciona a maior panqueca corretamente a cada passo.

