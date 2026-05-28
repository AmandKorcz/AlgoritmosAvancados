const filesInput = document.getElementById('files');
const patternInput = document.getElementById('pattern');
const algorithmSelect = document.getElementById('algorithm');
const resultsTable = document.getElementById('resultsTable');
const stepLog = document.getElementById('stepLog');
const bars = document.getElementById('bars');
const totalExecutions = document.getElementById('totalExecutions');
const algorithmCount = document.getElementById('algorithmCount');
const lastExecutionTime = document.getElementById('lastExecutionTime');

function validateForm() {
  if (!patternInput.value.trim()) {
    alert('Informe o pattern que será buscado.');
    return false;
  }

  if (!filesInput.files.length) {
    alert('Selecione pelo menos um arquivo .txt.');
    return false;
  }

  return true;
}

function createFormData(includeSteps = false) {
  const formData = new FormData();
  formData.append('pattern', patternInput.value);
  formData.append('include_steps', includeSteps);

  for (const file of filesInput.files) {
    formData.append('files', file);
  }

  return formData;
}

function renderResults(results) {
  resultsTable.innerHTML = '';

  for (const result of results) {
    const row = document.createElement('tr');
    row.innerHTML = `
      <td>${result.file_name || 'entrada manual'}</td>
      <td>${result.algorithm}</td>
      <td>${Number(result.execution_time_ms).toFixed(4)}</td>
      <td>${result.comparisons}</td>
      <td>${result.text_size}</td>
      <td>${result.pattern_size}</td>
      <td>${result.theoretical_complexity}</td>
      <td>${result.occurrences.join(', ') || '-'}</td>
    `;
    resultsTable.appendChild(row);
  }

  const first = results[0];
  if (first) {
    lastExecutionTime.textContent = `${Number(first.execution_time_ms).toFixed(4)} ms`;
  }
}

function renderSteps(results) {
  const resultWithSteps = results.find(result => result.steps && result.steps.length);

  if (!resultWithSteps) {
    stepLog.textContent = 'Nenhum passo foi retornado.';
    return;
  }

  stepLog.textContent = resultWithSteps.steps.join('\n');
}

async function executeSearch(includeSteps = false) {
  if (!validateForm()) return;

  const formData = createFormData(includeSteps);
  formData.append('algorithm', algorithmSelect.value);

  const response = await fetch('/api/search/files', {
    method: 'POST',
    body: formData,
  });

  if (!response.ok) {
    const error = await response.json();
    alert(error.detail || 'Erro ao executar busca.');
    return;
  }

  const data = await response.json();
  renderResults(data.results);

  if (includeSteps) {
    renderSteps(data.results);
  }

  await refreshDashboard();
}

async function compareAll() {
  if (!validateForm()) return;

  const formData = createFormData(false);

  const response = await fetch('/api/compare/files', {
    method: 'POST',
    body: formData,
  });

  if (!response.ok) {
    const error = await response.json();
    alert(error.detail || 'Erro ao comparar algoritmos.');
    return;
  }

  const data = await response.json();
  renderResults(data.results);
  stepLog.textContent = 'A comparação geral foi executada sem passo a passo para evitar logs muito grandes.';
  await refreshDashboard();
}

async function refreshDashboard() {
  const response = await fetch('/api/dashboard');
  const data = await response.json();

  totalExecutions.textContent = data.total_executions;
  algorithmCount.textContent = Object.keys(data.by_algorithm).length;
  bars.innerHTML = '';

  const algorithms = Object.entries(data.by_algorithm);
  const maxAverageTime = Math.max(...algorithms.map(([, item]) => item.average_execution_time_ms), 1);

  for (const [algorithm, item] of algorithms) {
    const percentage = Math.max(4, (item.average_execution_time_ms / maxAverageTime) * 100);
    const row = document.createElement('div');
    row.className = 'bar-row';
    row.innerHTML = `
      <div class="bar-label">
        <span>${algorithm}</span>
        <span>${item.executions} exec. · ${item.average_execution_time_ms.toFixed(4)} ms médio · ${Math.round(item.average_comparisons)} comp. médias</span>
      </div>
      <div class="bar-track">
        <div class="bar-fill" style="width: ${percentage}%"></div>
      </div>
    `;
    bars.appendChild(row);
  }

  if (!algorithms.length) {
    bars.innerHTML = '<p class="muted">Nenhuma execução registrada ainda.</p>';
  }
}

document.getElementById('runBtn').addEventListener('click', () => executeSearch(false));
document.getElementById('stepBtn').addEventListener('click', () => executeSearch(true));
document.getElementById('compareBtn').addEventListener('click', compareAll);
document.getElementById('refreshDashboardBtn').addEventListener('click', refreshDashboard);

refreshDashboard();
