import { AocInput } from "../AocInput";

const year = 2015;
const day = 1;

function part1(input: AocInput): number {
  const line = input.firstLine();
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

function part2(input: AocInput): number {
  const line = input.firstLine();
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

export { year, day, part1, part2 };
