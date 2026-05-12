import { MAX_WEIGHT } from "../data/items";

// Cria um cromossomo aleatório
function createRandomChromosome(itemsLength) {
  return Array.from({ length: itemsLength }, () => Math.round(Math.random()));
}

// Cria uma população inicial de forma aleatória
function createInitialPopulation(populationSize, itemsLength) {
  return Array.from({ length: populationSize }, () =>
    createRandomChromosome(itemsLength)
  );
}

// Calcula o peso total e a pontuação total de um cromossomo
function calculateChromosomeData(chromosome, items) {
  return chromosome.reduce(
    (total, gene, index) => {
      if (gene === 1) {
        total.weight += items[index].weight;
        total.points += items[index].points;
      }

      return total;
    },
    {
      weight: 0,
      points: 0,
    }
  );
}

// Função de fitness
// Maximiza a pontuação sem ultrapassar o limite de peso.
// Caso o peso ultrapasse 30kg, a solução é invalidada com fitness 0.
function calculateFitness(chromosome, items) {
  const chromosomeData = calculateChromosomeData(chromosome, items);

  if (chromosomeData.weight > MAX_WEIGHT) {
    return 0;
  }

  return chromosomeData.points;
}

// Avalia todos os indivíduos da população
function evaluatePopulation(population, items) {
  return population
    .map((chromosome) => {
      const chromosomeData = calculateChromosomeData(chromosome, items);

      return {
        chromosome,
        weight: chromosomeData.weight,
        points: chromosomeData.points,
        fitness: calculateFitness(chromosome, items),
      };
    })
    .sort((a, b) => b.fitness - a.fitness);
}

// Seleciona um indivíduo usando torneio
// Seleciona alguns indivíduos aleatórios e retorna o melhor entre eles
function tournamentSelection(evaluatedPopulation, tournamentSize = 3) {
  const selectedIndividuals = [];

  for (let i = 0; i < tournamentSize; i++) {
    const randomIndex = Math.floor(Math.random() * evaluatedPopulation.length);
    selectedIndividuals.push(evaluatedPopulation[randomIndex]);
  }

  selectedIndividuals.sort((a, b) => b.fitness - a.fitness);

  return selectedIndividuals[0].chromosome;
}

// Realiza o crossover de ponto único
function crossover(parentA, parentB) {
  const chromosomeLength = parentA.length;
  const crossoverPoint = Math.floor(Math.random() * (chromosomeLength - 1)) + 1;

  const child = [
    ...parentA.slice(0, crossoverPoint),
    ...parentB.slice(crossoverPoint),
  ];

  return child;
}

// Aplica mutação no cromossomo
function mutate(chromosome, mutationRate) {
  return chromosome.map((gene) => {
    const shouldMutate = Math.random() < mutationRate;

    if (shouldMutate) {
      return gene === 1 ? 0 : 1;
    }

    return gene;
  });
}

// Executa o algoritmo genético
export function runGeneticAlgorithm({
  items,
  populationSize,
  generations,
  mutationRate,
}) {
  let population = createInitialPopulation(populationSize, items.length);
  const fitnessHistory = [];

  for (let generation = 1; generation <= generations; generation++) {
    const evaluatedPopulation = evaluatePopulation(population, items);
    const bestIndividual = evaluatedPopulation[0];

    fitnessHistory.push({
      generation,
      bestFitness: bestIndividual.fitness,
      bestWeight: bestIndividual.weight,
      bestPoints: bestIndividual.points,
      bestChromosome: bestIndividual.chromosome.join(""),
    });

    const newPopulation = [];

    // Elitismo: mantém o melhor indivíduo da geração atual
    newPopulation.push(bestIndividual.chromosome);

    while (newPopulation.length < populationSize) {
      const parentA = tournamentSelection(evaluatedPopulation);
      const parentB = tournamentSelection(evaluatedPopulation);

      const child = crossover(parentA, parentB);
      const mutatedChild = mutate(child, mutationRate);

      newPopulation.push(mutatedChild);
    }

    population = newPopulation;
  }

  const finalEvaluatedPopulation = evaluatePopulation(population, items);
  const bestIndividual = finalEvaluatedPopulation[0];

  const selectedItems = items.filter(
    (_, index) => bestIndividual.chromosome[index] === 1
  );

  return {
    bestChromosome: bestIndividual.chromosome.join(""),
    totalWeight: bestIndividual.weight,
    totalPoints: bestIndividual.points,
    fitness: bestIndividual.fitness,
    selectedItems,
    fitnessHistory,
  };
}