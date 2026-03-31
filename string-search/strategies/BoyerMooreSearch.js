import SearchStrategy from "./SearchStrategy.js";

export default class BoyerMooreSearch extends SearchStrategy {
  buildBadCharTable(pattern) {
    const table = {};

    for (let i = 0; i < pattern.length; i++) {
      table[pattern[i]] = i;
    }

    return table;
  }

  search(text, pattern, stepMode = false) {
    const steps = [];
    const matches = [];
    let comparisons = 0;

    if (!pattern.length || pattern.length > text.length) {
      return {
        algorithm: "Boyer-Moore",
        matches,
        comparisons,
        textLength: text.length,
        patternLength: pattern.length,
        complexity: "O(n / m) melhor caso",
        steps,
        auxiliary: { badChar: {} }
      };
    }

    const badChar = this.buildBadCharTable(pattern);
    let shift = 0;

    if (stepMode) {
      steps.push("Construindo tabela de bad character...");
    }

    while (shift <= text.length - pattern.length) {
      let j = pattern.length - 1;

      if (stepMode) {
        steps.push(`Iniciando comparação com shift = ${shift}`);
      }

      while (j >= 0) {
        comparisons++;

        if (stepMode) {
          steps.push(`Comparando text[${shift + j}] = "${text[shift + j]}" com pattern[${j}] = "${pattern[j]}"`);
        }

        if (pattern[j] !== text[shift + j]) {
          break;
        }

        j--;
      }

      if (j < 0) {
        matches.push(shift);

        if (stepMode) {
          steps.push(`Padrão encontrado na posição ${shift}`);
        }

        shift += shift + pattern.length < text.length
          ? pattern.length - (badChar[text[shift + pattern.length]] ?? -1)
          : 1;
      } else {
        const badCharIndex = badChar[text[shift + j]];
        const jump = Math.max(1, j - (badCharIndex ?? -1));

        if (stepMode) {
          steps.push(`Falha. Caractere ruim: "${text[shift + j]}". Salto de ${jump}`);
        }

        shift += jump;
      }
    }

    return {
      algorithm: "Boyer-Moore",
      matches,
      comparisons,
      textLength: text.length,
      patternLength: pattern.length,
      complexity: "O(n / m) melhor caso",
      steps,
      auxiliary: { badChar }
    };
  }
}