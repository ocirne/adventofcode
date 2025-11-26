
pub struct FixedGrid {
    width: usize,
    height: usize,
    grid: Vec<usize>
}

impl FixedGrid {
    pub fn square(size: usize) -> FixedGrid {
        FixedGrid::rectangle(size, size)
    }

    pub fn rectangle(width: usize, height: usize) -> FixedGrid {
        FixedGrid { width, height, grid: vec![0; width * height] }
    }

    pub fn width(&self) -> usize {
        self.width
    }

    pub fn height(&self) -> usize {
        self.height
    }

    pub fn get(&self, x: usize, y: usize) -> usize {
        self.grid[x + y * self.height]
    }

    pub fn set(&mut self, x: usize, y: usize, value: usize) {
        self.grid[x + y * self.height] = value;
    }
}

// TODO DynamicGrid, basiert auf HashMap
