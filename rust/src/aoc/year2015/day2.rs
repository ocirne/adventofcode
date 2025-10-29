pub fn yd() -> (usize, usize) {
    (2015, 2)
}

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

fn solve<F>(data: &str, f: F) -> usize
where
    F: Fn(Dimensions) -> usize,
{
    let mut total = 0;
    let lines: Vec<&str> = data.split('\n').collect();
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

pub fn part1(data: &str) -> usize {
    solve(&data, |d| d.part1())
}

pub fn part2(data: &str) -> usize {
    solve(&data, |d| d.part2())
}
