use std::fs;

#[allow(unused)]
mod aoc;

use aoc::year2025::day1 as current;

fn main() {
    let (year, day) = current::yd();
    println!("Run AOC year {year} day {day}:");
    let filename = format!("../../adventofcode-input/resources/{year}/{day}/input");
    let data = fs::read_to_string(filename).expect("file error");
    println!("part1: {}", current::part1(&data));
    println!("part2: {}", current::part2(&data));
}
