use std::fs;

fn main() {
    const filename: &str = "../../../adventofcode-input/resources/2015/1/input";

    println!("Hello");

    let data = fs::read_to_string(filename).expect("Should be able to read file");
    let mut floor = 0;
    for c in data.chars() {
        match c {
            '(' => {
                //println!("open");
                floor += 1;
            }
            ')' => {
                //println!("close");
                floor -= 1;
            }
            other => {}
        }
    }
    println!("{floor}");

    let mut floor = 0;
    for (index, c) in data.chars().enumerate() {
        match c {
            '(' => {
                println!("open");
                floor += 1;
            }
            ')' => {
                println!("close");
                floor -= 1;
            }
            other => {}
        }
        if floor < 0 {
            println!("{}", index + 1);
            break;
        }
    }
}
