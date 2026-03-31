import SearchStrategy from "./SearchStrategy.js";

export default class NaiveSearch extends SearchStrategy {
  search(text, pattern, stepMode = false) {
    const steps = [];
    const matches = [];
    let comparisons = 0;

    if (!pattern.length || pattern.length > text.length) {
      return {
        algorithm: "Naive",
        matches,
        comparisons,
        textLength: text.length,
        patternLength: pattern.length,
        complexity: "O(n * m)",
        steps
      };
    }

    for (let i = 0; i <= text.length - pattern.length; i++) {
      let j = 0;

      if (stepMode) {
        steps.push(`Iniciando comparação na posição ${i}`);
      }

      while (j < pattern.length) {
        comparisons++;

        if (stepMode) {
          steps.push(`Comparando text[${i + j}] = "${text[i + j]}" com pattern[${j}] = "${pattern[j]}"`);
        }

        if (text[i + j] !== pattern[j]) {
          if (stepMode) {
            steps.push(`Falha na posição ${i + j}. Movendo padrão para ${i + 1}`);
          }
          break;
        }

        j++;
      }

      if (j === pattern.length) {
        matches.push(i);
        if (stepMode) {
          steps.push(`Padrão encontrado na posição ${i}`);
        }
      }
    }

    return {
      algorithm: "Naive",
      matches,
      comparisons,
      textLength: text.length,
      patternLength: pattern.length,
      complexity: "O(n * m)",
      steps
    };
  }
}