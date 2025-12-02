use std::cmp::max;
use std::collections::{HashMap, HashSet};

pub fn yd() -> (usize, usize) {
    (2025, 2)
}

const TEN: usize = 10;

fn lower_bound(a_str: &str) -> usize {
    if a_str.len() % 2 == 1 {
        return TEN.pow((a_str.len() / 2) as u32);
    }
    let l_a = a_str.len() / 2;
    let left = &a_str[..l_a].parse::<usize>().unwrap();
    let right = &a_str[l_a..].parse::<usize>().unwrap();
    if left < right { left + 1 } else { *left }
}

fn upper_bound(b_str: &str) -> usize {
    if b_str.len() % 2 == 1 {
        return TEN.pow(((b_str.len()-1) / 2) as u32) - 1;
    }
    let l_a = b_str.len() / 2;
    let left = &b_str[..l_a].parse::<usize>().unwrap();
    let right = &b_str[l_a..].parse::<usize>().unwrap();
    if left > right { left - 1 } else { *left }
}

fn foo(pair: &str) -> Option<usize> {
    let mut split = pair.split("-");
    let a_str = split.next().unwrap();
    let b_str = split.next().unwrap();
    let a_lb = lower_bound(a_str);
    let b_ub = upper_bound(b_str);
    if a_lb > b_ub {
        return None
    }
    let mut total = 0;
    for i in a_lb..=b_ub {
        total += i.to_string().repeat(2).parse::<usize>().unwrap();
    }
    Some(total)
}

fn lower_bound_n(a_str: &str, n: usize) -> usize {
    if a_str.len() % n != 0 {
        return TEN.pow((a_str.len() / n) as u32);
    }
    let l_a = a_str.len() / n;
    let left = &a_str[..l_a].parse::<usize>().unwrap();
    let a = a_str.parse::<usize>().unwrap();
    let cand = left.to_string().repeat(n).parse::<usize>().unwrap();
    if cand < a { left + 1 } else { *left }
}

fn upper_bound_n(b_str: &str, n: usize) -> usize {
    if b_str.len() % n != 0 {
        return TEN.pow(((b_str.len()-1) / n) as u32) - 1;
    }
    let l_a = b_str.len() / n;
    let left = &b_str[..l_a].parse::<usize>().unwrap();
    let b = b_str.parse::<usize>().unwrap();
    let cand = left.to_string().repeat(n).parse::<usize>().unwrap();
    if cand > b { left - 1 } else { *left }
}

fn foon(a_str: &str, b_str: &str, n: usize) -> HashSet<usize> {
    let a_lb = lower_bound_n(a_str, n);
    let b_ub = upper_bound_n(b_str, n);
    if a_lb > b_ub {
        return HashSet::new()
    }
    println!("{a_str}-{b_str}, {n} => {}-{}", a_lb.to_string().repeat(n).parse::<usize>().unwrap(), b_ub.to_string().repeat(n).parse::<usize>().unwrap());
    let mut total = HashSet::new();
    for i in a_lb..=b_ub {
        total.insert(i.to_string().repeat(n).parse::<usize>().unwrap());
    }
    total
}

fn foo2(pair: &str) -> Option<usize> {
    let mut split = pair.split("-");
    let a_str = split.next().unwrap();
    let b_str = split.next().unwrap();
    let mut total = HashSet::new();
    for n in 2..=b_str.len() {
        total.extend(foon(a_str, b_str, n));
    }
    println!("foo2 - {total:?}");
    Some(total.into_iter().sum())
}

pub fn part1(data: &str) -> usize {
    data.trim().split(",").filter_map(|pair| foo(pair)).sum()
}

pub fn part2(data: &str) -> usize {
    data.trim().split(",").filter_map(|pair| foo2(pair)).sum()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn tests_part1() {
        assert_eq!(foo("11-22"), Some(11 + 22));
        assert_eq!(foo("95-115"), Some(99));
        assert_eq!(foo("998-1012"), Some(1010));
        assert_eq!(foo("1188511880-1188511890"), Some(1188511885));
        assert_eq!(foo("222220-222224"), Some(222222));
        assert_eq!(foo("1698522-1698528"), None);
        assert_eq!(foo("446443-446449"), Some(446446));
        assert_eq!(foo("38593856-38593862"), Some(38593859));
        assert_eq!(foo("565653-565659"), None);
        assert_eq!(foo("824824821-824824827"), None);
        assert_eq!(foo("2121212118-2121212124"), None);
    }

    #[test]
    fn tests_part2() {
        assert_eq!(foo2("11-22"), Some(11 + 22));
        assert_eq!(foo2("95-115"), Some(99 + 111));
        assert_eq!(foo2("998-1012"), Some(999 + 1010));
        assert_eq!(foo2("1188511880-1188511890"), Some(1188511885));
        assert_eq!(foo2("222220-222224"), Some(222222));
        assert_eq!(foo2("1698522-1698528"), Some(0));
        assert_eq!(foo2("446443-446449"), Some(446446));
        assert_eq!(foo2("38593856-38593862"), Some(38593859));
        assert_eq!(foo2("565653-565659"), Some(565656));
        assert_eq!(foo2("824824821-824824827"), Some(824824824));
        assert_eq!(foo2("2121212118-2121212124"), Some(2121212121));
    }
}
