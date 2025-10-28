use std::collections::HashSet;
use std::fs;

fn solve(data: &str) -> usize {
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

fn main() {
    const FILENAME: &str = "../../../adventofcode-input/resources/2015/3/input";
    let data = fs::read_to_string(FILENAME).expect("file error");
    println!("{}", solve(&data));
}
