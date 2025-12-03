use std::ops::Index;

pub fn yd() -> (usize, usize) {
    (2025, 3)
}

fn battery_two(line: &str) -> usize {
    let digits: Vec<u32> = line.chars().map(|c| c.to_digit(10).unwrap()).collect();
    println!("{digits:?}");
    let r1 = &digits[..(digits.len() - 1)];
    let d1 = r1.iter().max().unwrap();
    println!("d1 {d1}");
    let i1 = digits.iter().position(|x| x == d1).unwrap();
    println!("i1 {i1}");
    let r2 = &digits[(i1+1)..];
    let d2 = r2.iter().max().unwrap();
    println!("d2 {d2}");
    (d1 * 10 + d2) as usize
}

fn rec(digits: &[u32], r: usize, acc: usize) -> usize {
    println!("{digits:?} {r}");
    if r == 0 {
        return acc
    }
    let range = &digits[..(digits.len() - r + 1)];
    let d = range.iter().max().unwrap();
    let i = digits.iter().position(|x| x == d).unwrap();
    rec(&digits[(i+1)..], r - 1, acc * 10 + (*d as usize))
}

fn battery_twelve(line: &str) -> usize {
    let digits: Vec<u32> = line.chars().map(|c| c.to_digit(10).unwrap()).collect();
    rec(digits.as_slice(), 12, 0)
}

pub fn part1(data: &str) -> usize {
    data.trim().lines().map(battery_two).sum()
}

pub fn part2(data: &str) -> usize {
    data.trim().lines().map(battery_twelve).sum()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn tests_part1() {
        assert_eq!(battery_two("987654321111111"), 98);
        assert_eq!(battery_two("811111111111119"), 89);
        assert_eq!(battery_two("234234234234278"), 78);
        assert_eq!(battery_two("818181911112111"), 92);
    }

    #[test]
    fn tests_part2() {
        assert_eq!(battery_twelve("987654321111111"), 987654321111);
        assert_eq!(battery_twelve("811111111111119"), 811111111119);
        assert_eq!(battery_twelve("234234234234278"), 434234234278);
        assert_eq!(battery_twelve("818181911112111"), 888911112111);
    }
}
