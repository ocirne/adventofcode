use std::fs;

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

fn main() {
    const FILENAME: &str = "../../../adventofcode-input/resources/2015/1/input";
    let data = fs::read_to_string(FILENAME).expect("file error");
    println!("{}", solve(&data, false));
    println!("{}", solve(&data, true));
}
