pub fn yd() -> (usize, usize) {
    (2015, 1)
}

fn solve(data: &str, part2: bool) -> isize {
    let mut floor = 0;
    for (index, c) in data.chars().enumerate() {
        floor += match c {
            '(' => 1,
            ')' => -1,
            _ => 0,
        };
        if part2 && floor < 0 {
            return (index + 1) as isize;
        }
    }
    floor
}

pub fn part1(data: &str) -> isize {
    solve(&data, false)
}

pub fn part2(data: &str) -> isize {
    solve(&data, true)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn tests_part1() {
        // (()) and ()() both result in floor 0
        assert_eq!(part1("(())"), 0);
        assert_eq!(part1("()()"), 0);
        // ((( and (()(()( both result in floor 3
        assert_eq!(part1("((("), 3);
        assert_eq!(part1("(()(()("), 3);
        // ))((((( also results in floor 3
        assert_eq!(part1("))((((("), 3);
        // ()) and ))( both result in floor -1 (the first basement level)
        assert_eq!(part1("())"), -1);
        assert_eq!(part1("))("), -1);
        // ))) and )())()) both result in floor -3
        assert_eq!(part1(")))"), -3);
        assert_eq!(part1(")())())"), -3);
    }

    #[test]
    fn tests_parts() {
        // ) causes him to enter the basement at character position 1
        assert_eq!(part2(")"), 1);
        // ()()) causes him to enter the basement at character position 5
        assert_eq!(part2("()())"), 5);
    }
}
