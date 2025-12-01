pub fn yd() -> (usize, usize) {
    (2025, 1)
}

pub fn part1(data: &str) -> usize {
    let mut result = 0;
    let mut p = 50;
    for line in data.lines() {
        if line.starts_with("L") {
            let d = line.strip_prefix("L").unwrap().parse::<isize>().unwrap();
            p -= d;
        } else if line.starts_with("R") {
            let d = line.strip_prefix("R").unwrap().parse::<isize>().unwrap();
            p += d;
        }
        p %= 100;
        if p == 0 {
            result += 1;
        }
    }
    result
}

pub fn part2(data: &str) -> isize {
    let mut result = 0;
    let mut p = 50;
    for line in data.lines() {
        if line.starts_with("L") {
            let d = line.strip_prefix("L").unwrap().parse::<isize>().unwrap();
            for i in 0..d {
                p -= 1;
                p %= 100;
                if p == 0 {
                    result += 1;
                }
            }
        } else if line.starts_with("R") {
            let d = line.strip_prefix("R").unwrap().parse::<isize>().unwrap();
            for i in 0..d {
                p += 1;
                p %= 100;
                if p == 0 {
                    result += 1;
                }
            }
        }
    }
    result
}

#[cfg(test)]
mod tests {
    use super::*;

    const INPUT: &str = "L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
";

    #[test]
    fn tests_part1() {
        assert_eq!(part1(INPUT), 3);
    }

    #[test]
    fn tests_part2() {
        assert_eq!(part2(INPUT), 6);
    }
}
