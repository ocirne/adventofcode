use std::collections::HashSet;

pub fn yd() -> (usize, usize) {
    (2025, 2)
}

const TEN: usize = 10;

fn repeat(n: &usize, times: usize) -> usize {
    n.to_string().repeat(times).parse::<usize>().unwrap()
}

fn lower_bound(a_str: &str, n: usize) -> usize {
    if a_str.len() % n != 0 {
        return TEN.pow((a_str.len() / n) as u32);
    }
    let a = a_str.parse::<usize>().unwrap();
    let len = a_str.len() / n;
    let first = &a_str[..len].parse::<usize>().unwrap();
    let cand = repeat(first, n);
    if cand < a {
        first + 1
    } else {
        *first
    }
}

fn upper_bound(b_str: &str, n: usize) -> usize {
    if b_str.len() % n != 0 {
        return TEN.pow(((b_str.len() - 1) / n) as u32) - 1;
    }
    let b = b_str.parse::<usize>().unwrap();
    let len = b_str.len() / n;
    let first = &b_str[..len].parse::<usize>().unwrap();
    let cand = repeat(first, n);
    if cand > b {
        first - 1
    } else {
        *first
    }
}

fn count_n(a_str: &str, b_str: &str, n: usize) -> HashSet<usize> {
    let a_lb = lower_bound(a_str, n);
    let b_ub = upper_bound(b_str, n);
    let mut total = HashSet::new();
    for i in a_lb..=b_ub {
        total.insert(repeat(&i, n));
    }
    total
}

fn count_two(pair: &str) -> usize {
    let mut split = pair.split("-");
    let a_str = split.next().unwrap();
    let b_str = split.next().unwrap();
    count_n(a_str, b_str, 2).into_iter().sum()
}

fn count_all(pair: &str) -> usize {
    let mut split = pair.split("-");
    let a_str = split.next().unwrap();
    let b_str = split.next().unwrap();
    let mut total = HashSet::new();
    for n in 2..=b_str.len() {
        total.extend(count_n(a_str, b_str, n));
    }
    total.into_iter().sum()
}

pub fn part1(data: &str) -> usize {
    data.trim().split(",").map(|pair| count_two(pair)).sum()
}

pub fn part2(data: &str) -> usize {
    data.trim().split(",").map(|pair| count_all(pair)).sum()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn tests_part1() {
        assert_eq!(count_two("11-22"), 11 + 22);
        assert_eq!(count_two("95-115"), 99);
        assert_eq!(count_two("998-1012"), 1010);
        assert_eq!(count_two("1188511880-1188511890"), 1188511885);
        assert_eq!(count_two("222220-222224"), 222222);
        assert_eq!(count_two("1698522-1698528"), 0);
        assert_eq!(count_two("446443-446449"), 446446);
        assert_eq!(count_two("38593856-38593862"), 38593859);
        assert_eq!(count_two("565653-565659"), 0);
        assert_eq!(count_two("824824821-824824827"), 0);
        assert_eq!(count_two("2121212118-2121212124"), 0);
    }

    #[test]
    fn tests_part2() {
        assert_eq!(count_all("11-22"), 11 + 22);
        assert_eq!(count_all("95-115"), 99 + 111);
        assert_eq!(count_all("998-1012"), 999 + 1010);
        assert_eq!(count_all("1188511880-1188511890"), 1188511885);
        assert_eq!(count_all("222220-222224"), 222222);
        assert_eq!(count_all("1698522-1698528"), 0);
        assert_eq!(count_all("446443-446449"), 446446);
        assert_eq!(count_all("38593856-38593862"), 38593859);
        assert_eq!(count_all("565653-565659"), 565656);
        assert_eq!(count_all("824824821-824824827"), 824824824);
        assert_eq!(count_all("2121212118-2121212124"), 2121212121);
    }
}
