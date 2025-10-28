use std::collections::HashSet;
use std::fs;

fn part1(data: &str) -> usize {
    let (mut x, mut y) = (0, 0);
    let mut houses = HashSet::new();
    houses.insert((x, y));
    for c in data.chars() {
        let (dx, dy) = match c {
            '^' => (0, -1),
            'v' => (0, 1),
            '<' => (-1, 0),
            '>' => (1, 0),
            _ => (0, 0),
        };
        x += dx;
        y += dy;
        houses.insert((x, y));
    }
    houses.len()
}

fn part2(data: &str) -> usize {
    let (mut x, mut y, mut rx, mut ry) = (0, 0, 0, 0);
    let mut houses = HashSet::new();
    houses.insert((x, y));
    for (index, c) in data.chars().enumerate() {
        let (dx, dy) = match c {
            '^' => (0, -1),
            'v' => (0, 1),
            '<' => (-1, 0),
            '>' => (1, 0),
            _ => (0, 0),
        };
        if index % 2 == 0 {
            x += dx;
            y += dy;
            houses.insert((x, y));
        } else {
            rx += dx;
            ry += dy;
            houses.insert((rx, ry));
        }
    }
    houses.len()
}

fn main() {
    const FILENAME: &str = "../../../adventofcode-input/resources/2015/3/input";
    let data = fs::read_to_string(FILENAME).expect("file error");
    println!("{}", part1(&data));
    println!("{}", part2(&data));
}
