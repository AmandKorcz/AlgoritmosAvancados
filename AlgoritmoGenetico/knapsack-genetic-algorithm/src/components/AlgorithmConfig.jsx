function AlgorithmConfig({ config, onChange, onRun }) {
  function handleChange(event) {
    const { name, value } = event.target;

    onChange({
      ...config,
      [name]: Number(value),
    });
  }

  return (
    <section className="card">
      <div className="card-header">
        <span className="card-label">Configurações</span>
        <h2>Parâmetros do algoritmo</h2>
        <p>
          Ajuste os valores usados pelo algoritmo genético para gerar, selecionar
          e evoluir as soluções.
        </p>
      </div>

      <div className="form-grid">
        <label>
          Tamanho da população
          <input
            type="number"
            name="populationSize"
            min="2"
            value={config.populationSize}
            onChange={handleChange}
          />
        </label>

        <label>
          Número de gerações
          <input
            type="number"
            name="generations"
            min="1"
            value={config.generations}
            onChange={handleChange}
          />
        </label>

        <label>
          Taxa de mutação
          <input
            type="number"
            name="mutationRate"
            min="0"
            max="1"
            step="0.01"
            value={config.mutationRate}
            onChange={handleChange}
          />
        </label>
      </div>

      <button className="primary-button" onClick={onRun}>
        Executar algoritmo
      </button>
    </section>
  );
}

export default AlgorithmConfig;