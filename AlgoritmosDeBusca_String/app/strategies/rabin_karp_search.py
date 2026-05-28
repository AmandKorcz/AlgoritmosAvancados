import time

from app.domain.search_result import SearchResult
from app.domain.search_strategy import SearchStrategy
from app.strategies._step_helper import add_step


class RabinKarpSearch(SearchStrategy):
    @property
    def name(self) -> str:
        return "Rabin-Karp"

    @property
    def theoretical_complexity(self) -> str:
        return "O(n + m) médio; O(n * m) pior caso"

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
        hash_checks = 0
        collisions = 0
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
                auxiliary_data={"hash_checks": 0, "collisions": 0},
                steps=steps,
            )

        base = 256
        prime = 101
        pattern_hash = 0
        window_hash = 0
        high_order = 1

        for _ in range(m - 1):
            high_order = (high_order * base) % prime

        for i in range(m):
            pattern_hash = (base * pattern_hash + ord(pattern[i])) % prime
            window_hash = (base * window_hash + ord(text[i])) % prime

        add_step(steps, f"Hash do padrão: {pattern_hash}.", include_steps, max_steps)

        for i in range(n - m + 1):
            hash_checks += 1
            add_step(steps, f"Janela {i}: hash_texto={window_hash}, hash_padrão={pattern_hash}.", include_steps, max_steps)

            if pattern_hash == window_hash:
                add_step(steps, "Hashes iguais. Confirmando caractere por caractere.", include_steps, max_steps)
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
                        collisions += 1
                        add_step(steps, "Colisão detectada: hash igual, texto diferente.", include_steps, max_steps)
                        break

                if match:
                    occurrences.append(i)
                    add_step(steps, f"Ocorrência encontrada na posição {i}.", include_steps, max_steps)

            if i < n - m:
                window_hash = (
                    base * (window_hash - ord(text[i]) * high_order) + ord(text[i + m])
                ) % prime

                if window_hash < 0:
                    window_hash += prime

        elapsed_ms = (time.perf_counter_ns() - start) / 1_000_000
        return SearchResult(
            algorithm=self.name,
            occurrences=occurrences,
            comparisons=comparisons,
            execution_time_ms=elapsed_ms,
            text_size=n,
            pattern_size=m,
            theoretical_complexity=self.theoretical_complexity,
            auxiliary_data={
                "base": base,
                "prime": prime,
                "pattern_hash": pattern_hash,
                "hash_checks": hash_checks,
                "collisions": collisions,
            },
            steps=steps,
        )
