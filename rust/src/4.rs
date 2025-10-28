use md5;
use std::fs;

fn solve(data: &str, target: &str) -> usize {
    let mut i = 0;
    loop {
        let digest = md5::compute(data.to_owned() + &i.to_string());
        if format!("{digest:x}").starts_with(target) {
            return i;
        }
        i += 1;
    }
}

fn main() {
    const FILENAME: &str = "/home/enrico/github/adventofcode-input/resources/2015/4/input";
    let data = fs::read_to_string(FILENAME).expect("file error");
    println!("{}", solve(&data, "00000"));
    println!("{}", solve(&data, "000000"));
}
