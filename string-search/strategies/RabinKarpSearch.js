import SearchStrategy from "./SearchStrategy.js";

export default class RabinKarpSearch extends SearchStrategy {
  search(text, pattern, stepMode = false) {
    const steps = [];
    const matches = [];
    let comparisons = 0;

    const m = pattern.length;
    const n = text.length;
    const base = 256;
    const prime = 101;

    if (!pattern.length || pattern.length > text.length) {
      return {
        algorithm: "Rabin-Karp",
        matches,
        comparisons,
        textLength: text.length,
        patternLength: pattern.length,
        complexity: "O(n + m) médio",
        steps
      };
    }

    let patternHash = 0;
    let windowHash = 0;
    let h = 1;

    for (let i = 0; i < m - 1; i++) {
      h = (h * base) % prime;
    }

    for (let i = 0; i < m; i++) {
      patternHash = (base * patternHash + pattern.charCodeAt(i)) % prime;
      windowHash = (base * windowHash + text.charCodeAt(i)) % prime;
    }

    for (let i = 0; i <= n - m; i++) {
      if (stepMode) {
        steps.push(`Janela ${i}: hashPattern=${patternHash}, hashTexto=${windowHash}`);
      }

      if (patternHash === windowHash) {
        if (stepMode) {
          steps.push(`Hashes iguais na posição ${i}. Verificando caracteres...`);
        }

        let match = true;

        for (let j = 0; j < m; j++) {
          comparisons++;

          if (stepMode) {
            steps.push(`Comparando text[${i + j}] = "${text[i + j]}" com pattern[${j}] = "${pattern[j]}"`);
          }

          if (text[i + j] !== pattern[j]) {
            match = false;

            if (stepMode) {
              steps.push(`Colisão de hash detectada na posição ${i}`);
            }

            break;
          }
        }

        if (match) {
          matches.push(i);

          if (stepMode) {
            steps.push(`Padrão encontrado na posição ${i}`);
          }
        }
      }

      if (i < n - m) {
        windowHash = (
          base * (windowHash - text.charCodeAt(i) * h) +
          text.charCodeAt(i + m)
        ) % prime;

        if (windowHash < 0) {
          windowHash += prime;
        }
      }
    }

    return {
      algorithm: "Rabin-Karp",
      matches,
      comparisons,
      textLength: text.length,
      patternLength: pattern.length,
      complexity: "O(n + m) médio",
      steps
    };
  }
}