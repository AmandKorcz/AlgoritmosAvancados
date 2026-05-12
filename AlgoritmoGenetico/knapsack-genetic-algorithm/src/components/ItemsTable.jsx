function ItemsTable({ items }) {
  return (
    <section className="card">
      <div className="card-header">
        <span className="card-label">Itens disponíveis</span>
        <h2>Tabela de sobrevivência</h2>
        <p>
          Cada item possui um peso e uma pontuação de sobrevivência. O algoritmo
          deve escolher a melhor combinação sem ultrapassar 30 kg.
        </p>
      </div>

      <div className="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Item</th>
              <th>Peso</th>
              <th>Pontuação</th>
            </tr>
          </thead>

          <tbody>
            {items.map((item) => (
              <tr key={item.name}>
                <td>{item.name}</td>
                <td>{item.weight} kg</td>
                <td>{item.points} pts</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  );
}

export default ItemsTable;