import { expect, test } from "vitest";
import { direct, input } from "./AocInput";
import { part1, part2 } from "./Day1";

test("basics", () => {
  expect(part1(direct("("))).toBe(1);
  expect(part1(direct(")"))).toBe(-1);
});

test("examples part1", () => {
  // (()) and ()() both result in floor 0.
  expect(part1(direct("(())"))).toBe(0);
  expect(part1(direct("()()"))).toBe(0);

  // ((( and (()(()( both result in floor 3.
  expect(part1(direct("((("))).toBe(3);
  expect(part1(direct("(()(()("))).toBe(3);

  // ))((((( also results in floor 3.
  expect(part1(direct("))((((("))).toBe(3);

  // ()) and ))( both result in floor -1 (the first basement level).
  expect(part1(direct("())"))).toBe(-1);
  expect(part1(direct("))("))).toBe(-1);

  // ))) and )())()) both result in floor -3.
  expect(part1(direct(")))"))).toBe(-3);
  expect(part1(direct(")())())"))).toBe(-3);
});

test("examples part2", () => {
  // ) causes him to enter the basement at character position 1.
  expect(part2(direct(")"))).toBe(1);

  // ()()) causes him to enter the basement at character position 5.
  expect(part2(direct("()())"))).toBe(5);
});

test("acceptance part1", () => {
  expect(part1(input(2015, 1))).toBe(280);
});

test("acceptance part2", () => {
  expect(part2(input(2015, 1))).toBe(1797);
});
