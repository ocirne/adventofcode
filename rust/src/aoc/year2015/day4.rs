use md5;

pub fn yd() -> (usize, usize) {
    (2015, 4)
}

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

pub fn part1(data: &str) -> usize {
    solve(&data, "00000")
}

pub fn part2(data: &str) -> usize {
    solve(&data, "000000")
}
