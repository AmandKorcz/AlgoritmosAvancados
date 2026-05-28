import time
from typing import Dict

from app.domain.search_result import SearchResult
from app.domain.search_strategy import SearchStrategy
from app.strategies._step_helper import add_step


class BoyerMooreSearch(SearchStrategy):
    @property
    def name(self) -> str:
        return "Boyer-Moore"

    @property
    def theoretical_complexity(self) -> str:
        return "O(n / m) melhor caso; O(n * m) pior caso"

    def _build_bad_character_table(self, pattern: str) -> Dict[str, int]:
        return {char: index for index, char in enumerate(pattern)}

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
                auxiliary_data={"bad_character_table": {}},
                steps=steps,
            )

        bad_character_table = self._build_bad_character_table(pattern)
        add_step(steps, f"Tabela Bad Character criada: {bad_character_table}.", include_steps, max_steps)

        shift = 0
        while shift <= n - m:
            j = m - 1
            add_step(steps, f"Alinhando padrão na posição {shift}.", include_steps, max_steps)

            while j >= 0:
                comparisons += 1
                add_step(
                    steps,
                    f"Comparando texto[{shift + j}]='{text[shift + j]}' com padrão[{j}]='{pattern[j]}'.",
                    include_steps,
                    max_steps,
                )

                if pattern[j] != text[shift + j]:
                    break
                j -= 1

            if j < 0:
                occurrences.append(shift)
                add_step(steps, f"Ocorrência encontrada na posição {shift}.", include_steps, max_steps)

                if shift + m < n:
                    next_char = text[shift + m]
                    shift_amount = m - bad_character_table.get(next_char, -1)
                else:
                    shift_amount = 1

                add_step(steps, f"Deslocando {shift_amount} posição(ões).", include_steps, max_steps)
                shift += shift_amount
            else:
                mismatched_char = text[shift + j]
                last_occurrence = bad_character_table.get(mismatched_char, -1)
                shift_amount = max(1, j - last_occurrence)
                add_step(
                    steps,
                    f"Falha com caractere '{mismatched_char}'. Deslocando {shift_amount} posição(ões).",
                    include_steps,
                    max_steps,
                )
                shift += shift_amount

        elapsed_ms = (time.perf_counter_ns() - start) / 1_000_000
        return SearchResult(
            algorithm=self.name,
            occurrences=occurrences,
            comparisons=comparisons,
            execution_time_ms=elapsed_ms,
            text_size=n,
            pattern_size=m,
            theoretical_complexity=self.theoretical_complexity,
            auxiliary_data={"bad_character_table": bad_character_table},
            steps=steps,
        )
