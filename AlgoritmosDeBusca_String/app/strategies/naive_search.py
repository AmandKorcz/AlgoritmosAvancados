import time

from app.domain.search_result import SearchResult
from app.domain.search_strategy import SearchStrategy
from app.strategies._step_helper import add_step


class NaiveSearch(SearchStrategy):
    @property
    def name(self) -> str:
        return "Naive"

    @property
    def theoretical_complexity(self) -> str:
        return "O(n * m)"

    def search(
        self,
        text: str,
        pattern: str,
        include_steps: bool = False,
        max_steps: int = 300,
    ) -> SearchResult:
        start = time.perf_counter_ns()
        occurrences = []
        comparisons = 0
        steps = []

        n = len(text)
        m = len(pattern)

        if m == 0 or n == 0 or m > n:
            elapsed_ms = (time.perf_counter_ns() - start) / 1_000_000
            return SearchResult(
                algorithm=self.name,
                occurrences=[],
                comparisons=0,
                execution_time_ms=elapsed_ms,
                text_size=n,
                pattern_size=m,
                theoretical_complexity=self.theoretical_complexity,
                auxiliary_data={"observation": "Texto vazio, padrão vazio ou padrão maior que o texto."},
                steps=steps,
            )

        for i in range(n - m + 1):
            add_step(steps, f"Alinhando padrão na posição {i} do texto.", include_steps, max_steps)
            match = True

            for j in range(m):
                comparisons += 1
                add_step(
                    steps,
                    f"Comparando texto[{i + j}]='{text[i + j]}' com padrão[{j}]='{pattern[j]}'.",
                    include_steps,
                    max_steps,
                )

                if text[i + j] != pattern[j]:
                    match = False
                    add_step(steps, "Falha na comparação. Deslocando uma posição.", include_steps, max_steps)
                    break

            if match:
                occurrences.append(i)
                add_step(steps, f"Ocorrência encontrada na posição {i}.", include_steps, max_steps)

        elapsed_ms = (time.perf_counter_ns() - start) / 1_000_000
        return SearchResult(
            algorithm=self.name,
            occurrences=occurrences,
            comparisons=comparisons,
            execution_time_ms=elapsed_ms,
            text_size=n,
            pattern_size=m,
            theoretical_complexity=self.theoretical_complexity,
            auxiliary_data={"strategy": "Força bruta com deslocamento de uma posição por tentativa."},
            steps=steps,
        )
