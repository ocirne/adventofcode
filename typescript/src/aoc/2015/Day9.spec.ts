import { expect, test } from "vitest";
import { loadExample } from "../AocInput";
import { part1, part2 } from "./Day9";

test("examples part1", () => {
  expect(part1(loadExample(2015, 9))).toBe(605);
});

test("examples part2", () => {
  expect(part2(loadExample(2015, 9))).toBe(982);
});
