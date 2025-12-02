use std::cmp::max;

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
    println!("{a_str}-{b_str} -> {a_lb}{a_lb}-{b_ub}{b_ub}");
    if a_lb > b_ub {
        return None
    }
    let mut total = 0;
    for i in a_lb..=b_ub {
        println!("i {i}");
        total += format!("{i}{i}").parse::<usize>().unwrap();
    }
    Some(total)
}

pub fn part1(data: &str) -> usize {
    data.trim().split(",").filter_map(|pair| foo(pair)).sum()
}

pub fn part2(data: &str) -> usize {
1
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn tests_part1() {
        assert_eq!(foo("11-22"), Some(33));
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
    }
}
