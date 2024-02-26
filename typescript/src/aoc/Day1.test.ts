
import { expect, test } from 'vitest';
import Day1 from './Day1';

test('basics', () => {
    const day1 = new Day1('');
    expect(day1.part1('(')).toBe(1);
    expect(day1.part1(')')).toBe(-1);
});

test('examples part1', () => {
    const day1 = new Day1('');

    // (()) and ()() both result in floor 0.
    expect(day1.part1('(())')).toBe(0);
    expect(day1.part1('()()')).toBe(0);
    
    // ((( and (()(()( both result in floor 3.
    expect(day1.part1('(((')).toBe(3);
    expect(day1.part1('(()(()(')).toBe(3);

    // ))((((( also results in floor 3.
    expect(day1.part1('))(((((')).toBe(3);

    // ()) and ))( both result in floor -1 (the first basement level).
    expect(day1.part1('())')).toBe(-1);
    expect(day1.part1('))(')).toBe(-1);

    // ))) and )())()) both result in floor -3.
    expect(day1.part1(')))')).toBe(-3);
    expect(day1.part1(')())())')).toBe(-3);
});

test('examples part2', () => {
    const day1 = new Day1('');

    // ) causes him to enter the basement at character position 1. 
    expect(day1.part2(')')).toBe(1);

    // ()()) causes him to enter the basement at character position 5.
    expect(day1.part2('()())')).toBe(5);
});

test('acceptance part1', () => {
    const day1 = new Day1('');
    expect(day1.part1('')).toBe(0);
});

test('acceptance part2', () => {
    const day1 = new Day1('');

    expect(day1.part2('')).toBe(0);
});
