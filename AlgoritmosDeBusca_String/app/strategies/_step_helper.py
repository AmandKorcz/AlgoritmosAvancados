from typing import List


def add_step(steps: List[str], message: str, include_steps: bool, max_steps: int) -> None:
    """Adiciona uma linha ao log passo a passo respeitando um limite máximo.

    Em arquivos grandes, guardar todos os passos pode deixar a resposta pesada.
    Por isso, o log é limitado. A execução normal continua analisando o texto
    completo, apenas o log visual é resumido.
    """

    if not include_steps:
        return

    if len(steps) < max_steps:
        steps.append(message)
    elif len(steps) == max_steps:
        steps.append("... log limitado para evitar resposta muito grande ...")
