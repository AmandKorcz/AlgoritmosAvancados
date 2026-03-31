import NaiveSearch from "./strategies/NaiveSearch.js";
import RabinKarpSearch from "./strategies/RabinKarpSearch.js";
import KMPSearch from "./strategies/KMPSearch.js";
import BoyerMooreSearch from "./strategies/BoyerMooreSearch.js";
import SearchContext from "./context/SearchContext.js";
import { readFiles } from "./utils/fileReader.js";

function getStrategy(name) {
  if (name === "naive") return new NaiveSearch();
  if (name === "rabinKarp") return new RabinKarpSearch();
  if (name === "kmp") return new KMPSearch();
  if (name === "boyerMoore") return new BoyerMooreSearch();
  throw new Error("Algoritmo inválido.");
}

function validateInputs(files, pattern) {
  if (!files.length) {
    alert("Selecione pelo menos um arquivo .txt.");
    return false;
  }

  if (!pattern) {
    alert("Digite um pattern para buscar.");
    return false;
  }

  return true;
}

function renderSingleResult(result, fileName) {
  return `
    <div class="result-card">
      <p><strong>Arquivo:</strong> ${fileName}</p>
      <p><strong>Algoritmo:</strong> ${result.algorithm}</p>
      <p><strong>Tempo:</strong> ${result.executionTime} ms</p>
      <p><strong>Comparações:</strong> ${result.comparisons}</p>
      <p><strong>Tamanho do texto:</strong> ${result.textLength}</p>
      <p><strong>Tamanho do padrão:</strong> ${result.patternLength}</p>
      <p><strong>Complexidade teórica:</strong> ${result.complexity}</p>
      <p><strong>Ocorrências:</strong> ${result.matches.length ? result.matches.join(", ") : "Nenhuma ocorrência encontrada"}</p>
    </div>
  `;
}

window.runSearch = async function () {
  const files = document.getElementById("fileInput").files;
  const pattern = document.getElementById("patternInput").value;
  const algorithm = document.getElementById("algorithmSelect").value;
  const resultsDiv = document.getElementById("results");
  const log = document.getElementById("log");

  log.textContent = "";

  if (!validateInputs(files, pattern)) return;

  const fileContents = await readFiles(files);
  const strategy = getStrategy(algorithm);
  const context = new SearchContext(strategy);

  resultsDiv.innerHTML = "";

  for (const file of fileContents) {
    const start = performance.now();
    const result = context.execute(file.content, pattern, false);
    const end = performance.now();

    result.executionTime = (end - start).toFixed(4);
    resultsDiv.innerHTML += renderSingleResult(result, file.name);
  }
};

window.runStepByStep = async function () {
  const files = document.getElementById("fileInput").files;
  const pattern = document.getElementById("patternInput").value;
  const algorithm = document.getElementById("algorithmSelect").value;
  const resultsDiv = document.getElementById("results");
  const log = document.getElementById("log");

  if (!validateInputs(files, pattern)) return;

  const fileContents = await readFiles(files);
  const strategy = getStrategy(algorithm);
  const context = new SearchContext(strategy);

  resultsDiv.innerHTML = "";
  log.textContent = "";

  for (const file of fileContents) {
    const start = performance.now();
    const result = context.execute(file.content, pattern, true);
    const end = performance.now();

    result.executionTime = (end - start).toFixed(4);
    resultsDiv.innerHTML += renderSingleResult(result, file.name);

    log.textContent += `========== Arquivo: ${file.name} ==========\n`;
    result.steps.forEach(step => {
      log.textContent += `${step}\n`;
    });

    if (result.auxiliary) {
      log.textContent += "\nEstruturas auxiliares:\n";
      log.textContent += `${JSON.stringify(result.auxiliary, null, 2)}\n`;
    }

    log.textContent += "\n";
  }
};

window.compareAll = async function () {
  const files = document.getElementById("fileInput").files;
  const pattern = document.getElementById("patternInput").value;
  const resultsDiv = document.getElementById("results");
  const log = document.getElementById("log");

  log.textContent = "";

  if (!validateInputs(files, pattern)) return;

  const fileContents = await readFiles(files);
  const algorithms = ["naive", "rabinKarp", "kmp", "boyerMoore"];

  resultsDiv.innerHTML = "";

  for (const file of fileContents) {
    let tableRows = "";

    for (const algo of algorithms) {
      const strategy = getStrategy(algo);
      const context = new SearchContext(strategy);

      const start = performance.now();
      const result = context.execute(file.content, pattern, false);
      const end = performance.now();

      result.executionTime = (end - start).toFixed(4);

      tableRows += `
        <tr>
          <td>${result.algorithm}</td>
          <td>${result.executionTime}</td>
          <td>${result.comparisons}</td>
          <td>${result.textLength}</td>
          <td>${result.patternLength}</td>
          <td>${result.complexity}</td>
          <td>${result.matches.length ? result.matches.join(", ") : "Nenhuma"}</td>
        </tr>
      `;
    }

    resultsDiv.innerHTML += `
      <div class="result-card">
        <p><strong>Arquivo:</strong> ${file.name}</p>
        <table class="compare-table">
          <thead>
            <tr>
              <th>Algoritmo</th>
              <th>Tempo (ms)</th>
              <th>Comparações</th>
              <th>Tam. texto</th>
              <th>Tam. padrão</th>
              <th>Complexidade</th>
              <th>Ocorrências</th>
            </tr>
          </thead>
          <tbody>
            ${tableRows}
          </tbody>
        </table>
      </div>
    `;
  }
};