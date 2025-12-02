pub fn yd() -> (usize, usize) {
    (2025, 1)
}

struct Dial {
    position: isize,
    total: usize,
}

impl Dial {
    fn part1(&self, delta: isize) -> Self {
        let p1 = (self.position + delta) % 100;
        let total1 = self.total + (p1 == 0) as usize;
        Dial {
            position: p1,
            total: total1,
        }
    }

    fn part2(&self, delta: isize) -> Self {
        let p1 = (self.position + delta) % 100;
        let s = (delta.signum() * self.position).rem_euclid(100) + delta.abs();
        let total1 = self.total + (s / 100) as usize;
        Dial {
            position: p1,
            total: total1,
        }
    }
}

fn solve<F>(data: &str, f: F) -> usize
where
    F: Fn(Dial, isize) -> Dial,
{
    let data = data.replace("L", "-").replace("R", "+");
    let mut dial = Dial {
        position: 50,
        total: 0,
    };
    for line in data.lines() {
        let delta = line.parse::<isize>().unwrap();
        dial = f(dial, delta)
    }
    dial.total
}

pub fn part1(data: &str) -> usize {
    solve(data, |dial, delta| dial.part1(delta))
}

pub fn part2(data: &str) -> usize {
    solve(data, |dial, delta| dial.part2(delta))
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
