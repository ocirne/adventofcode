use std::fs;

fn main() {
    const filename: &str = "../../../adventofcode-input/resources/2015/1/input";

    println!("Hello");

    let data = fs::read_to_string(filename).expect("Should be able to read file");
    let mut i = 0;
    for c in data.chars() {
        match c {
            '(' => {
                println!("open");
                i += 1;
            }
            ')' => {
                println!("close");
                i -= 1;
            }
            other => {}
        }
    }
    println!("{i}");
}
