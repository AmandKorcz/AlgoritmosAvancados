import time
from typing import List

from app.domain.search_result import SearchResult
from app.domain.search_strategy import SearchStrategy
from app.strategies._step_helper import add_step


class KMPSearch(SearchStrategy):
    @property
    def name(self) -> str:
        return "KMP"

    @property
    def theoretical_complexity(self) -> str:
        return "O(n + m)"

    def _build_lps(self, pattern: str) -> List[int]:
        lps = [0] * len(pattern)
        length = 0
        i = 1

        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            elif length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

        return lps

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
                auxiliary_data={"lps": []},
                steps=steps,
            )

        lps = self._build_lps(pattern)
        add_step(steps, f"Tabela LPS criada: {lps}.", include_steps, max_steps)

        i = 0  # índice do texto
        j = 0  # índice do padrão

        while i < n:
            comparisons += 1
            add_step(
                steps,
                f"Comparando texto[{i}]='{text[i]}' com padrão[{j}]='{pattern[j]}'.",
                include_steps,
                max_steps,
            )

            if text[i] == pattern[j]:
                i += 1
                j += 1

                if j == m:
                    occurrence = i - j
                    occurrences.append(occurrence)
                    add_step(steps, f"Ocorrência encontrada na posição {occurrence}.", include_steps, max_steps)
                    j = lps[j - 1]
                    add_step(steps, f"Usando LPS para reposicionar j em {j}.", include_steps, max_steps)
            else:
                if j != 0:
                    j = lps[j - 1]
                    add_step(steps, f"Falha. Usando LPS para reposicionar j em {j}.", include_steps, max_steps)
                else:
                    i += 1
                    add_step(steps, "Falha com j=0. Avançando no texto.", include_steps, max_steps)

        elapsed_ms = (time.perf_counter_ns() - start) / 1_000_000
        return SearchResult(
            algorithm=self.name,
            occurrences=occurrences,
            comparisons=comparisons,
            execution_time_ms=elapsed_ms,
            text_size=n,
            pattern_size=m,
            theoretical_complexity=self.theoretical_complexity,
            auxiliary_data={"lps": lps},
            steps=steps,
        )
