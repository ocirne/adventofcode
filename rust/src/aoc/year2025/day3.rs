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

pub fn part1(data: &str) -> usize {
    data.trim().lines().map(battery_two).sum()
}

pub fn part2(data: &str) -> usize {
    1
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
    }
}
