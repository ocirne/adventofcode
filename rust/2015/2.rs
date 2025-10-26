use std::fs;

fn part1(lines: &Vec<&str>) -> usize {
    let mut total = 0;
    for line in lines {
        if line.is_empty() {
            continue;
        }
        let mut n: Vec<usize> = line
            .split('x')
            .map(|s| s.parse::<usize>().unwrap())
            .collect();
        n.sort();
        let (l, w, h) = (n[0], n[1], n[2]);
        total += 3 * l * w + 2 * l * h + 2 * w * h;
    }
    total
}

fn part2(lines: &Vec<&str>) -> usize {
    let mut total = 0;
    for line in lines {
        if line.is_empty() {
            continue;
        }
        let mut n: Vec<usize> = line
            .split('x')
            .map(|s| s.parse::<usize>().unwrap())
            .collect();
        n.sort();
        let (l, w, h) = (n[0], n[1], n[2]);
        total += 2 * l + 2 * w + l * w * h;
    }
    total
}

fn main() {
    const FILENAME: &str = "../../../adventofcode-input/resources/2015/2/input";
    let data = fs::read_to_string(FILENAME).expect("file error");
    let lines = data.split('\n').collect();
    println!("{}", part1(&lines));
    println!("{}", part2(&lines));
}
