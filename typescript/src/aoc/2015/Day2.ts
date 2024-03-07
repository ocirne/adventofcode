import { AocInput } from "../AocInput";

const year = 2015;
const day = 2;

function unpackLine(line: string): [number, number, number] {
  const [l, w, h] = line
    .split("x")
    .map((i) => parseInt(i))
    .sort((a, b) => a - b);
  return [l, w, h];
}

function wrappingPaper(l: number, w: number, h: number): number {
  return 3 * l * w + 2 * w * h + 2 * h * l;
}

function ribbon(l: number, w: number, h: number): number {
  return 2 * l + 2 * w + l * w * h;
}

function findOrder(
  input: AocInput,
  fun: (l: number, w: number, h: number) => number,
): number {
  return input
    .splitLines()
    .reduce((total, line) => total + fun(...unpackLine(line)), 0);
}

function part1(input: AocInput): number {
  return findOrder(input, wrappingPaper);
}

function part2(input: AocInput): number {
  return findOrder(input, ribbon);
}

export { year, day, part1, part2 };
