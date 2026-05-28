export default class SearchContext {
  constructor(strategy) {
    this.strategy = strategy;
  }

  setStrategy(strategy) {
    this.strategy = strategy;
  }

  execute(text, pattern, stepMode = false) {
    return this.strategy.search(text, pattern, stepMode);
  }
}