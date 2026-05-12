import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  CartesianGrid,
} from "recharts";

function FitnessChart({ history }) {
  if (!history || history.length === 0) {
    return (
      <section className="card chart-card">
        <span className="card-label">Evolução</span>
        <h2>Fitness por geração</h2>
        <p>
          Execute o algoritmo para visualizar a evolução do melhor fitness ao
          longo das gerações.
        </p>
      </section>
    );
  }

  return (
    <section className="card chart-card">
      <div className="card-header">
        <span className="card-label">Evolução</span>
        <h2>Fitness por geração</h2>
        <p>
          O gráfico mostra como a melhor solução encontrada evoluiu durante a
          execução do algoritmo genético.
        </p>
      </div>

      <div className="chart-wrapper">
        <ResponsiveContainer width="100%" height={280}>
          <LineChart data={history}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis
              dataKey="generation"
              label={{
                value: "Geração",
                position: "insideBottom",
                offset: -5,
              }}
            />
            <YAxis
              label={{
                value: "Fitness",
                angle: -90,
                position: "insideLeft",
              }}
            />
            <Tooltip />
            <Line
              type="monotone"
              dataKey="bestFitness"
              strokeWidth={3}
              dot={false}
              name="Melhor fitness"
            />
          </LineChart>
        </ResponsiveContainer>
      </div>
    </section>
  );
}

export default FitnessChart;