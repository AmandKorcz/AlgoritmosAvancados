import SearchStrategy from "./SearchStrategy.js";

export default class KMPSearch extends SearchStrategy {
  buildLPS(pattern, steps, stepMode) {
    const lps = Array(pattern.length).fill(0);
    let len = 0;
    let i = 1;

    if (stepMode) {
      steps.push("Construindo tabela LPS...");
    }

    while (i < pattern.length) {
      if (pattern[i] === pattern[len]) {
        len++;
        lps[i] = len;

        if (stepMode) {
          steps.push(`LPS[${i}] = ${len}`);
        }

        i++;
      } else if (len !== 0) {
        len = lps[len - 1];

        if (stepMode) {
          steps.push(`Falha ao montar LPS. Atualizando len para ${len}`);
        }
      } else {
        lps[i] = 0;

        if (stepMode) {
          steps.push(`LPS[${i}] = 0`);
        }

        i++;
      }
    }

    return lps;
  }

  search(text, pattern, stepMode = false) {
    const steps = [];
    const matches = [];
    let comparisons = 0;

    if (!pattern.length || pattern.length > text.length) {
      return {
        algorithm: "KMP",
        matches,
        comparisons,
        textLength: text.length,
        patternLength: pattern.length,
        complexity: "O(n + m)",
        steps,
        auxiliary: { lps: [] }
      };
    }

    const lps = this.buildLPS(pattern, steps, stepMode);

    let i = 0;
    let j = 0;

    while (i < text.length) {
      comparisons++;

      if (stepMode) {
        steps.push(`Comparando text[${i}] = "${text[i]}" com pattern[${j}] = "${pattern[j]}"`);
      }

      if (text[i] === pattern[j]) {
        i++;
        j++;
      }

      if (j === pattern.length) {
        matches.push(i - j);

        if (stepMode) {
          steps.push(`Padrão encontrado na posição ${i - j}`);
        }

        j = lps[j - 1];

        if (stepMode) {
          steps.push(`Atualizando j com LPS: ${j}`);
        }
      } else if (i < text.length && text[i] !== pattern[j]) {
        if (j !== 0) {
          j = lps[j - 1];

          if (stepMode) {
            steps.push(`Falha. Reposicionando j com LPS: ${j}`);
          }
        } else {
          i++;

          if (stepMode) {
            steps.push(`Falha com j = 0. Avançando i para ${i}`);
          }
        }
      }
    }

    return {
      algorithm: "KMP",
      matches,
      comparisons,
      textLength: text.length,
      patternLength: pattern.length,
      complexity: "O(n + m)",
      steps,
      auxiliary: { lps }
    };
  }
}