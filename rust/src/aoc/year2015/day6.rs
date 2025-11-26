use crate::aoc::util::FixedGrid;

pub fn yd() -> (usize, usize) {
    (2015, 6)
}

struct LightGrid {
    grid: FixedGrid
}

impl LightGrid {
    fn new(size: usize) -> LightGrid {
        LightGrid { grid: FixedGrid::square(size) }
    }

    fn light<F>(&mut self, coords: (usize, usize, usize, usize), f: F)
    where
        F: Fn(usize) -> usize
    {
        let (x0, y0, x1, y1) = coords;
        for x in x0..=x1 {
            for y in y0..=y1 {
                let value = f(self.grid.get(x, y));
                self.grid.set(x, y, value);
            }
        }
    }

    fn count_lit(&self) -> usize {
        let mut result = 0;
        for x in 0..self.grid.width() {
            for y in 0..self.grid.height() {
                result += self.grid.get(x, y);
            }
        }
        result
    }
}

fn get_xy(xy: &str) -> (usize, usize) {
    let xy: Vec<&str> = xy.split(",").collect();
    (xy[0].parse::<usize>().unwrap(), xy[1].parse::<usize>().unwrap())
}

fn parse_line(line: &str, i0: usize, i1: usize) -> (usize, usize, usize, usize) {
    let token: Vec<&str> = line.split(" ").collect();
    let (x0, y0) = get_xy(token[i0]);
    let (x1, y1) = get_xy(token[i1]);
    (x0, y0, x1, y1)
}

fn solve<F, G, H>(data: &str, fn_on: F, fn_off: G, fn_toggle: H) -> usize
where
    F: Fn(usize) -> usize,
    G: Fn(usize) -> usize,
    H: Fn(usize) -> usize
{
    let mut grid = LightGrid::new(1000);
    for line in data.lines() {
        match line {
            line if line.starts_with("turn on") => grid.light(parse_line(line, 2, 4), &fn_on),
            line if line.starts_with("turn off") => grid.light(parse_line(line, 2, 4), &fn_off),
            line if line.starts_with("toggle") => grid.light(parse_line(line, 1, 3), &fn_toggle),
            _ => {}
        }
    }
    grid.count_lit()
}

pub fn part1(data: &str) -> usize {
    let fn_on = |_| 1;
    let fn_off = |_| 0;
    let fn_toggle = |v: usize /* Type */| 1 - v;
    solve(data, fn_on, fn_off, fn_toggle)
}

pub fn part2(data: &str) -> usize {
    let fn_on = |v: usize /* Type */| v + 1;
    let fn_off = |v: usize /* Type */| if v > 0 { v - 1 } else { v };
    let fn_toggle = |v: usize /* Type */| v + 2;
    solve(data, fn_on, fn_off, fn_toggle)
}
