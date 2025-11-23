
pub fn yd() -> (usize, usize) {
    (2015, 6)
}

fn get_xy(xy: &str) -> (usize, usize) {
    let xy: Vec<&str> = xy.split(",").collect();
    (xy[0].parse::<usize>().unwrap(), xy[1].parse::<usize>().unwrap())
}

fn light<F>(grid: &mut [[usize; 1000]; 1000], line: &str, i0: usize, i1: usize, f: F)
where
    F: Fn(usize) -> usize
{
    let token: Vec<&str> = line.split(" ").collect();
    let (x0, y0) = get_xy(token[i0]);
    let (x1, y1) = get_xy(token[i1]);
    for x in x0..=x1 {
        for y in y0..=y1 {
            grid[x][y] = f(grid[x][y])
        }
    }
}

fn count_lit(grid: &[[usize; 1000]; 1000]) -> usize {
    let mut result = 0;
    for x in 0..1000 {
        for y in 0..1000 {
            result += grid[x][y];
        }
    }
    result
}

fn solve<F, G, H>(data: &str, fn_on: F, fn_off: G, fn_toggle: H) -> usize
where
    F: Fn(usize) -> usize,
    G: Fn(usize) -> usize,
    H: Fn(usize) -> usize
{
    let mut grid = [[0; 1000] ; 1000];
    for line in data.lines() {
        match line {
            line if line.starts_with("turn on") => light(&mut grid, line, 2, 4, &fn_on),
            line if line.starts_with("turn off") => light(&mut grid, line, 2, 4, &fn_off),
            line if line.starts_with("toggle") => light(&mut grid, line, 1, 3, &fn_toggle),
            _ => {}
        }
    }
    count_lit(&grid)
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
