import { expect, test } from "vitest";
import { readFileSync } from "fs";
import Day2 from "./Day2";

test("examples part1", () => {
  const day2 = new Day2([""]);

  expect(day2.part1_single("2x3x4")).toBe(58);
  expect(day2.part1_single("1x1x10")).toBe(43);
});

test("examples part2", () => {
  const day2 = new Day2([""]);

  expect(day2.part2_single("2x3x4")).toBe(34);
  expect(day2.part2_single("1x1x10")).toBe(14);
});

test("acceptance part1", () => {
  const data = readFileSync(
    "../../adventofcode-input/resources/2015/2/input",
    "utf8",
  );
  const day2 = new Day2(data.trim().split("\n"));
  expect(day2.part1()).toBe(1598415);
});

test("acceptance part2", () => {
  const data = readFileSync(
    "../../adventofcode-input/resources/2015/2/input",
    "utf8",
  );
  const day2 = new Day2(data.trim().split("\n"));
  expect(day2.part2()).toBe(3812909);
});
