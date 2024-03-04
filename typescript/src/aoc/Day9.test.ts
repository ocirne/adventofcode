import { expect, test } from "vitest";
import { example, input } from "./AocInput";
import { part1, part2 } from "./Day9";

test("examples part1", () => {
  expect(part1(example(2015, 9))).toBe(605);
});

test("examples part2", () => {
  expect(part2(example(2015, 9))).toBe(982);
});

test("acceptance part1", () => {
  expect(part1(input(2015, 9))).toBe(117);
});

test("acceptance part2", () => {
  expect(part2(input(2015, 9))).toBe(909);
});
