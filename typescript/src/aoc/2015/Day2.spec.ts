import { expect, test } from "vitest";
import { direct } from "../AocInput";
import { part1, part2 } from "./Day2";

test("examples part1", () => {
  expect(part1(direct("2x3x4"))).toBe(58);
  expect(part1(direct("1x1x10"))).toBe(43);
});

test("examples part2", () => {
  expect(part2(direct("2x3x4"))).toBe(34);
  expect(part2(direct("1x1x10"))).toBe(14);
});
