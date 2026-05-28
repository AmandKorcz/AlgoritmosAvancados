from abc import ABC, abstractmethod

from app.domain.search_result import SearchResult


class SearchStrategy(ABC):
    """Contrato comum para os algoritmos de busca.

    Cada algoritmo concreto implementa esse contrato, permitindo que o serviço
    escolha a estratégia em tempo de execução sem conhecer os detalhes internos.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def theoretical_complexity(self) -> str:
        pass

    @abstractmethod
    def search(
        self,
        text: str,
        pattern: str,
        include_steps: bool = False,
        max_steps: int = 300,
    ) -> SearchResult:
        pass
