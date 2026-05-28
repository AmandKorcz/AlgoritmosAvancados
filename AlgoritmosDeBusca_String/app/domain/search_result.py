from dataclasses import asdict, dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class SearchResult:
    """Retorno padronizado para todos os algoritmos de busca.

    Essa estrutura é importante para aplicar o padrão Strategy de forma limpa:
    cada algoritmo pode ter uma implementação interna diferente, mas todos
    devolvem os mesmos campos para a camada de serviço, API e dashboard.
    """

    algorithm: str
    occurrences: List[int]
    comparisons: int
    execution_time_ms: float
    text_size: int
    pattern_size: int
    theoretical_complexity: str
    auxiliary_data: Dict[str, Any] = field(default_factory=dict)
    steps: List[str] = field(default_factory=list)
    file_name: Optional[str] = None

    @property
    def occurrences_count(self) -> int:
        return len(self.occurrences)

    def to_dict(self) -> Dict[str, Any]:
        data = asdict(self)
        data["occurrences_count"] = self.occurrences_count
        return data
