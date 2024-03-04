import { expect, test } from "vitest";
import { input } from "./AocInput";
import { part1 as day1part1, part2 as day1part2 } from "./Day1";
import { part1 as day2part1, part2 as day2part2 } from "./Day2";
import { part1 as day9part1, part2 as day9part2 } from "./Day9";


test("acceptance day 1 part1", () => {
  expect(day1part1(input(2015, 1))).toBe(280);
});

test("acceptance day 1 part2", () => {
  expect(day1part2(input(2015, 1))).toBe(1797);
});

test("acceptance day 2 part1", () => {
  expect(day2part1(input(2015, 2))).toBe(1598415);
});
  
test("acceptance day 2 part2", () => {
    expect(day2part2(input(2015, 2))).toBe(3812909);
});  

test("acceptance day 9 part1", () => {
  expect(day9part1(input(2015, 9))).toBe(117);
});

test("acceptance day 9 part2", () => {
  expect(day9part2(input(2015, 9))).toBe(909);
});
