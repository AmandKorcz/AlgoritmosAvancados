import logging
from typing import Dict, List

from app.domain.search_result import SearchResult
from app.domain.search_strategy import SearchStrategy
from app.observability.telemetry import get_metric, get_tracer
from app.services.dashboard_repository import dashboard_repository
from app.strategies.boyer_moore_search import BoyerMooreSearch
from app.strategies.kmp_search import KMPSearch
from app.strategies.naive_search import NaiveSearch
from app.strategies.rabin_karp_search import RabinKarpSearch

logger = logging.getLogger(__name__)


class SearchService:
    """Camada de aplicação responsável por orquestrar as estratégias de busca."""

    def __init__(self) -> None:
        self._strategies: Dict[str, SearchStrategy] = {
            "naive": NaiveSearch(),
            "rabin-karp": RabinKarpSearch(),
            "kmp": KMPSearch(),
            "boyer-moore": BoyerMooreSearch(),
        }

    def available_algorithms(self) -> List[Dict[str, str]]:
        return [
            {
                "key": key,
                "name": strategy.name,
                "theoretical_complexity": strategy.theoretical_complexity,
            }
            for key, strategy in self._strategies.items()
        ]

    def execute(
        self,
        algorithm: str,
        text: str,
        pattern: str,
        file_name: str | None = None,
        include_steps: bool = False,
    ) -> SearchResult:
        strategy = self._strategies.get(algorithm)

        if strategy is None:
            raise ValueError(f"Algoritmo inválido: {algorithm}")

        tracer = get_tracer()
        attributes = {
            "algorithm": strategy.name,
            "text_size": len(text),
            "pattern_size": len(pattern),
            "file_name": file_name or "entrada_manual",
        }

        logger.info(
            "Iniciando busca | algoritmo=%s | arquivo=%s | text_size=%s | pattern_size=%s",
            strategy.name,
            file_name or "entrada_manual",
            len(text),
            len(pattern),
        )

        with tracer.start_as_current_span("search.execution") as span:
            for key, value in attributes.items():
                span.set_attribute(key, value)

            result = strategy.search(text=text, pattern=pattern, include_steps=include_steps)
            result.file_name = file_name

            span.set_attribute("comparisons", result.comparisons)
            span.set_attribute("occurrences_count", result.occurrences_count)
            span.set_attribute("execution_time_ms", result.execution_time_ms)

        metric_attributes = {"algorithm": strategy.name}
        get_metric("search_execution_total").add(1, metric_attributes)
        get_metric("search_execution_time_ms").record(result.execution_time_ms, metric_attributes)
        get_metric("search_comparisons_total").add(result.comparisons, metric_attributes)
        get_metric("search_occurrences_total").add(result.occurrences_count, metric_attributes)

        dashboard_repository.record(result)

        logger.info(
            "Busca finalizada | algoritmo=%s | tempo_ms=%.4f | comparacoes=%s | ocorrencias=%s",
            strategy.name,
            result.execution_time_ms,
            result.comparisons,
            result.occurrences_count,
        )

        return result

    def compare_all(
        self,
        text: str,
        pattern: str,
        file_name: str | None = None,
    ) -> List[SearchResult]:
        return [
            self.execute(key, text, pattern, file_name=file_name, include_steps=False)
            for key in self._strategies.keys()
        ]


search_service = SearchService()
