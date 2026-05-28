function ResultCard({ result }) {
  if (!result) {
    return (
      <section className="card result-empty">
        <span className="card-label">Resultado</span>
        <h2>Aguardando execução</h2>
        <p>
          Configure os parâmetros e execute o algoritmo para encontrar a melhor
          combinação de itens para a mochila.
        </p>
      </section>
    );
  }

  return (
    <section className="card result-card">
      <div className="card-header">
        <span className="card-label">Resultado</span>
        <h2>Melhor solução encontrada</h2>
        <p>
          Esta é a melhor combinação encontrada pelo algoritmo genético dentro
          do limite de peso da mochila.
        </p>
      </div>

      <div className="result-grid">
        <div className="metric">
          <span>Cromossomo</span>
          <strong>{result.bestChromosome}</strong>
        </div>

        <div className="metric">
          <span>Peso total</span>
          <strong>{result.totalWeight} kg</strong>
        </div>

        <div className="metric">
          <span>Pontuação total</span>
          <strong>{result.totalPoints} pts</strong>
        </div>

        <div className="metric">
          <span>Fitness</span>
          <strong>{result.fitness}</strong>
        </div>
      </div>

      <div className="selected-items">
        <h3>Itens selecionados</h3>

        {result.selectedItems.length > 0 ? (
          <ul>
            {result.selectedItems.map((item) => (
              <li key={item.name}>
                <span>{item.name}</span>
                <small>
                  {item.weight} kg • {item.points} pts
                </small>
              </li>
            ))}
          </ul>
        ) : (
          <p>Nenhum item foi selecionado.</p>
        )}
      </div>
    </section>
  );
}

export default ResultCard;