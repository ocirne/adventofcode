pub fn yd() -> (usize, usize) {
    (2025, 3)
}

fn rec(digits: &[usize], r: usize, acc: usize) -> usize {
    if r == 0 {
        return acc
    }
    let range = &digits[..(digits.len() - r + 1)];
    let digit = range.iter().max().unwrap();
    let index = digits.iter().position(|x| x == digit).unwrap();
    rec(&digits[(index+1)..], r - 1, acc * 10 + digit)
}

fn battery(line: &str, n: usize) -> usize {
    let digits: Vec<usize> = line.chars().map(|c| c.to_digit(10).unwrap() as usize).collect();
    rec(digits.as_slice(), n, 0)
}

fn solve(data: &str, n: usize) -> usize {
    data.trim().lines().map(|line| battery(line, n)).sum()
}

pub fn part1(data: &str) -> usize {
    solve(data, 2)
}

pub fn part2(data: &str) -> usize {
    solve(data, 12)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn tests_part1() {
        assert_eq!(battery("987654321111111", 2), 98);
        assert_eq!(battery("811111111111119", 2), 89);
        assert_eq!(battery("234234234234278", 2), 78);
        assert_eq!(battery("818181911112111", 2), 92);
    }

    #[test]
    fn tests_part2() {
        assert_eq!(battery("987654321111111", 12), 987654321111);
        assert_eq!(battery("811111111111119", 12), 811111111119);
        assert_eq!(battery("234234234234278", 12), 434234234278);
        assert_eq!(battery("818181911112111", 12), 888911112111);
    }
}
