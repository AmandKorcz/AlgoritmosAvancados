import { useState } from "react";

import AlgorithmConfig from "./components/AlgorithmConfig";
import FitnessChart from "./components/FitnessChart";
import ItemsTable from "./components/ItemsTable";
import ResultCard from "./components/ResultCard";

import { items, MAX_WEIGHT } from "./data/items";
import { runGeneticAlgorithm } from "./genetic/geneticAlgorithm";

function App() {
  const [config, setConfig] = useState({
    populationSize: 20,
    generations: 50,
    mutationRate: 0.05,
  });

  const [result, setResult] = useState(null);

  function handleRunAlgorithm() {
    const algorithmResult = runGeneticAlgorithm({
      items,
      populationSize: config.populationSize,
      generations: config.generations,
      mutationRate: config.mutationRate,
    });

    setResult(algorithmResult);
  }

  return (
    <main className="app">
      <section className="hero">
        <span className="eyebrow">Knapsack Problem</span>

        <h1>Algoritmo Genético para o Problema da Mochila</h1>

        <p>
          Aplicação acadêmica que utiliza algoritmo genético para encontrar a
          melhor combinação de itens de sobrevivência, respeitando a capacidade
          máxima de {MAX_WEIGHT} kg da mochila.
        </p>
      </section>

      <section className="layout">
        <div className="left-column">
          <ItemsTable items={items} />

          <AlgorithmConfig
            config={config}
            onChange={setConfig}
            onRun={handleRunAlgorithm}
          />
        </div>

        <div className="right-column">
          <ResultCard result={result} />
        </div>
      </section>

      <FitnessChart history={result?.fitnessHistory} />
    </main>
  );
}

export default App;