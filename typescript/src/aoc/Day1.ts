class Day1 {
  constructor(lines: string) {}

  public part1(line: string): number {
    let total = 0;
    for (let i = 0; i < line.length; i++) {
      if (line[i] == "(") {
        total++;
      } else if (line[i] == ")") {
        total--;
      }
    }
    return total;
  }

  public part2(line: string): number {
    let total = 0;
    for (let i = 0; i < line.length; i++) {
      if (line[i] == "(") {
        total++;
      } else if (line[i] == ")") {
        total--;
      }
      if (total < 0) {
        return i + 1;
      }
    }
    return total;
  }
}

export default Day1;
