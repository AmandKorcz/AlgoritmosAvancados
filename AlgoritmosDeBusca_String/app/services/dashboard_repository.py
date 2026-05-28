from collections import defaultdict, deque
from typing import Any, Deque, Dict, List

from app.domain.search_result import SearchResult


class DashboardRepository:
    """Armazena métricas de execução em memória para o dashboard da atividade.

    A proposta é simples para facilitar a entrega acadêmica. Em um ambiente real,
    essas informações poderiam ser enviadas para Prometheus, Grafana, Loki,
    Jaeger ou outro backend de observabilidade.
    """

    def __init__(self, max_items: int = 500):
        self._history: Deque[Dict[str, Any]] = deque(maxlen=max_items)

    def record(self, result: SearchResult) -> None:
        self._history.appendleft(result.to_dict())

    def list_history(self) -> List[Dict[str, Any]]:
        return list(self._history)

    def summary(self) -> Dict[str, Any]:
        by_algorithm = defaultdict(
            lambda: {
                "executions": 0,
                "total_execution_time_ms": 0.0,
                "total_comparisons": 0,
                "total_occurrences": 0,
                "average_execution_time_ms": 0.0,
                "average_comparisons": 0.0,
            }
        )

        for item in self._history:
            algorithm = item["algorithm"]
            stats = by_algorithm[algorithm]
            stats["executions"] += 1
            stats["total_execution_time_ms"] += item["execution_time_ms"]
            stats["total_comparisons"] += item["comparisons"]
            stats["total_occurrences"] += item["occurrences_count"]

        for stats in by_algorithm.values():
            executions = stats["executions"] or 1
            stats["average_execution_time_ms"] = stats["total_execution_time_ms"] / executions
            stats["average_comparisons"] = stats["total_comparisons"] / executions

        return {
            "total_executions": len(self._history),
            "by_algorithm": dict(by_algorithm),
            "last_results": list(self._history)[:10],
        }


dashboard_repository = DashboardRepository()
