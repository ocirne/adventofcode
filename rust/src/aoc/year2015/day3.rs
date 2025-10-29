use std::collections::HashSet;

pub fn yd() -> (usize, usize) {
    (2015, 3)
}

#[derive(Copy, Clone)]
struct Santa {
    x: isize,
    y: isize,
}

impl Santa {
    fn move_santa(self, c: char) -> Self {
        let (dx, dy) = match c {
            '^' => (0, -1),
            'v' => (0, 1),
            '<' => (-1, 0),
            '>' => (1, 0),
            _ => (0, 0),
        };
        Santa {
            x: self.x + dx,
            y: self.y + dy,
        }
    }
    fn position(self) -> (isize, isize) {
        (self.x, self.y)
    }
}

pub fn part1(data: &str) -> usize {
    let mut santa = Santa { x: 0, y: 0 };
    let mut houses = HashSet::new();
    houses.insert(santa.position());
    for c in data.chars() {
        santa = santa.move_santa(c);
        houses.insert(santa.position());
    }
    houses.len()
}

pub fn part2(data: &str) -> usize {
    let mut santa = Santa { x: 0, y: 0 };
    let mut robot_santa = Santa { x: 0, y: 0 };
    let mut houses = HashSet::new();
    houses.insert(santa.position());
    for (index, c) in data.chars().enumerate() {
        if index % 2 == 0 {
            santa = santa.move_santa(c);
            houses.insert(santa.position());
        } else {
            robot_santa = robot_santa.move_santa(c);
            houses.insert(robot_santa.position());
        }
    }
    houses.len()
}
