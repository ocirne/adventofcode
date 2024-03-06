import { expect, test } from "vitest";
import AocInput, { input } from "./AocInput";
// import { part1 as day1part1, part2 as day1part2 } from "./Day1";
import { part1 as day2part1, part2 as day2part2 } from "./Day2";
import { part1 as day9part1, part2 as day9part2 } from "./Day9";
import { readFileSync } from "fs";

// test("acceptance day 1 part1", () => {
//   expect(day1part1(input(2015, 1))).toBe(280);
// });

// test("acceptance day 1 part2", () => {
//   expect(day1part2(input(2015, 1))).toBe(1797);
// });

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


import { globSync } from 'glob';

import { parse } from 'csv-parse/sync';

function loadResult(year: number, day: number) {
  const results = readFileSync(
    `../../adventofcode-input/resources/results${year}.csv`,
    "utf8",
  );

  const records = parse(results, {
    columns: true,
    skip_empty_lines: true
  });

  return records.find((baz:any) => baz.day == day);
}

test("foo", async() => {
let modules;
console.log("blub");
const path = __dirname + '/Day[129].ts';
console.log('path', path);
const res = globSync(path);
for (let j = 0; j < res.length; j++) {
  const file = res[j];
  const i = file.replace(__dirname, '.').replace('.ts', '');
  console.log("import", i, 'from', file);
  const { year, day, part1, part2 } = await import(file.replace(__dirname, '.').replace('.ts', ''));
  const data = input(year, day);
  const result = loadResult(year, day);
  console.log(result);
  console.log(result.part1);
  console.log(result.part2);
  console.log(part1(data).toString());
  console.log(part2(data).toString());
   expect(part1(data).toString()).toBe(result.part1);
   expect(part2(data).toString()).toBe(result.part2);
}});
