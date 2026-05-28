from app.strategies.boyer_moore_search import BoyerMooreSearch
from app.strategies.kmp_search import KMPSearch
from app.strategies.naive_search import NaiveSearch
from app.strategies.rabin_karp_search import RabinKarpSearch


def test_algorithms_find_same_occurrences_for_simple_text():
    text = "algoritmo de busca em strings usa algoritmo"
    pattern = "algoritmo"
    expected = [0, 34]

    strategies = [NaiveSearch(), RabinKarpSearch(), KMPSearch(), BoyerMooreSearch()]

    for strategy in strategies:
        result = strategy.search(text, pattern)

        assert result.occurrences == expected
        assert result.comparisons > 0
        assert result.text_size == len(text)
        assert result.pattern_size == len(pattern)


def test_algorithms_return_empty_occurrences_when_pattern_does_not_exist():
    text = "estrutura de dados e algoritmos"
    pattern = "banana"

    strategies = [NaiveSearch(), RabinKarpSearch(), KMPSearch(), BoyerMooreSearch()]

    for strategy in strategies:
        result = strategy.search(text, pattern)

        assert result.occurrences == []
        assert result.occurrences_count == 0
        assert result.execution_time_ms >= 0


def test_step_by_step_returns_logs():
    result = NaiveSearch().search("abcabc", "abc", include_steps=True)

    assert result.occurrences == [0, 3]
    assert len(result.steps) > 0
    assert "Comparando" in "\n".join(result.steps)
