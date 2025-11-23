
pub fn yd() -> (usize, usize) {
    (2015, 6)
}

fn foo(xy: &str) -> (usize, usize) {
    let xy: Vec<&str> = xy.split(",").collect();
    (xy[0].parse::<usize>().unwrap(), xy[1].parse::<usize>().unwrap())
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

pub fn part1(data: &str) -> usize {
    let mut grid = [[0; 1000] ; 1000];
    for line in data.lines() {
        if line.starts_with("turn on") {
            let token: Vec<&str> = line.split(" ").collect();
            let (x0, y0) = foo(token[2]);
            let (x1, y1) = foo(token[4]);
            for x in x0..=x1 {
                for y in y0..=y1 {
                    grid[x][y] = 1;
                }
            }
        }
        else if line.starts_with("turn off") {
            let token: Vec<&str> = line.split(" ").collect();
            let (x0, y0) = foo(token[2]);
            let (x1, y1) = foo(token[4]);
            for x in x0..=x1 {
                for y in y0..=y1 {
                    grid[x][y] = 0;
                }
            }
        }
        else if line.starts_with("toggle") {
            let token: Vec<&str> = line.split(" ").collect();
            let (x0, y0) = foo(token[1]);
            let (x1, y1) = foo(token[3]);
            for x in x0..=x1 {
                for y in y0..=y1 {
                    grid[x][y] = 1 - grid[x][y];
                }
            }
        }
    }
    count_lit(&grid)
}

pub fn part2(data: &str) -> usize {
    let mut grid = [[0; 1000] ; 1000];
    for line in data.lines() {
        if line.starts_with("turn on") {
            let token: Vec<&str> = line.split(" ").collect();
            let (x0, y0) = foo(token[2]);
            let (x1, y1) = foo(token[4]);
            for x in x0..=x1 {
                for y in y0..=y1 {
                    grid[x][y] += 1;
                }
            }
        }
        else if line.starts_with("turn off") {
            let token: Vec<&str> = line.split(" ").collect();
            let (x0, y0) = foo(token[2]);
            let (x1, y1) = foo(token[4]);
            for x in x0..=x1 {
                for y in y0..=y1 {
                    if grid[x][y] > 0 {
                        grid[x][y] = grid[x][y] - 1;
                    }
                }
            }
        }
        else if line.starts_with("toggle") {
            let token: Vec<&str> = line.split(" ").collect();
            let (x0, y0) = foo(token[1]);
            let (x1, y1) = foo(token[3]);
            for x in x0..=x1 {
                for y in y0..=y1 {
                    grid[x][y] = grid[x][y] + 2;
                }
            }
        }
    }
    count_lit(&grid)
}
