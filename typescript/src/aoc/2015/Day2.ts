import { AocInput } from "../AocInput";

const year = 2015;
const day = 2;

function part1_single(line: string): number {
  const [l, w, h] = line
    .split("x")
    .map((i) => parseInt(i))
    .sort((a, b) => a - b);
  return 3 * l * w + 2 * w * h + 2 * h * l;
}

function part1(input: AocInput): number {
  return input.rawData
    .trim()
    .split("\n")
    .reduce((total, line) => total + part1_single(line), 0);
}

// The ribbon required to wrap a present is the shortest distance around its sides, or the smallest perimeter of any one face.
// the feet of ribbon required for the perfect bow is equal to the cubic feet of volume of the present.

function part2_single(line: string): number {
  const [l, w, h] = line
    .split("x")
    .map((i) => parseInt(i))
    .sort((a, b) => a - b);
  return 2 * l + 2 * w + l * w * h;
}

function part2(input: AocInput): number {
  return input.rawData
    .trim()
    .split("\n")
    .reduce((total, line) => total + part2_single(line), 0);
}

export { year, day, part1, part2 };
