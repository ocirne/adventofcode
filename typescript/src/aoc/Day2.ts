class Day2 {
  readonly lines: string[];

  constructor(lines: string[]) {
    this.lines = lines;
  }

  public part1_single(line: string): number {
    const [l, w, h] = line
      .split("x")
      .map((i) => parseInt(i))
      .sort((a, b) => a - b);
    return 3 * l * w + 2 * w * h + 2 * h * l;
  }

  public part1(): number {
    return this.lines.reduce(
      (total, line) => total + this.part1_single(line),
      0,
    );
  }

  // The ribbon required to wrap a present is the shortest distance around its sides, or the smallest perimeter of any one face.
  // the feet of ribbon required for the perfect bow is equal to the cubic feet of volume of the present.

  public part2_single(line: string): number {
    const [l, w, h] = line
      .split("x")
      .map((i) => parseInt(i))
      .sort((a, b) => a - b);
    return 2 * l + 2 * w + l * w * h;
  }

  public part2(): number {
    return this.lines.reduce(
      (total, line) => total + this.part2_single(line),
      0,
    );
  }
}

export default Day2;
