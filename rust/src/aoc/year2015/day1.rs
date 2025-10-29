use std::fs;

pub fn yd() -> (usize, usize) {
    (2015, 1)
}

fn solve(data: &str, part2: bool) -> isize {
    let mut floor = 0;
    for (index, c) in data.chars().enumerate() {
        floor += match c {
            '(' => 1,
            ')' => -1,
            _ => 0,
        };
        if part2 && floor < 0 {
            return (index + 1) as isize;
        }
    }
    floor
}

pub fn part1(data: &str) -> isize {
    solve(&data, false)
}

pub fn part2(data: &str) -> isize {
    solve(&data, true)
}
