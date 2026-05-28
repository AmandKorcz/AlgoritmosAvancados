import json
from pathlib import Path

from app.services.search_service import search_service


def main() -> None:
    data_dir = Path("data/arquivos_teste")
    output_dir = Path("results")
    output_dir.mkdir(exist_ok=True)

    pattern = "algoritmo"
    results = []

    for file_path in data_dir.glob("*.txt"):
        text = file_path.read_text(encoding="utf-8", errors="ignore")
        for result in search_service.compare_all(text=text, pattern=pattern, file_name=file_path.name):
            results.append(result.to_dict())

    output_file = output_dir / "benchmark_results.json"
    output_file.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Benchmark finalizado. Resultados salvos em: {output_file}")


if __name__ == "__main__":
    main()
