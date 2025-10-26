use std::fs;

struct Dimensions {
    l: usize,
    w: usize,
    h: usize,
}

impl Dimensions {
    fn part1(&self) -> usize {
        3 * self.l * self.w + 2 * self.l * self.h + 2 * self.w * self.h
    }

    fn part2(&self) -> usize {
        2 * self.l + 2 * self.w + self.l * self.w * self.h
    }
}

fn solve<F>(lines: &Vec<&str>, f: F) -> usize
where
    F: Fn(Dimensions) -> usize,
{
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
        let d = Dimensions {
            l: n[0],
            w: n[1],
            h: n[2],
        };
        total += f(d);
    }
    total
}

fn main() {
    const FILENAME: &str = "../../../adventofcode-input/resources/2015/2/input";
    let data = fs::read_to_string(FILENAME).expect("file error");
    let lines = data.split('\n').collect();
    println!("{}", solve(&lines, |d| d.part1()));
    println!("{}", solve(&lines, |d| d.part2()));
}
