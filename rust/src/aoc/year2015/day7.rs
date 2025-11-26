use std::collections::HashMap;
use std::num::ParseIntError;

pub fn yd() -> (usize, usize) {
    (2015, 7)
}

fn foo(wires: &HashMap<&str, u16>, token: &str) -> Result<u16, ParseIntError> {
    match token.parse::<u16>() {
        Ok(value) => Ok(value),
        ParseIntError => {
            if wires.contains_key(token) {
                Ok(wires[token])
            } else {
                ParseIntError
            }
        }
    }
}

fn part1_internal(data: &str, b: u16) -> HashMap<&str, u16> {
    let mut wires: HashMap<&str, u16> = HashMap::new();
    if b > 0 {
        wires.insert("b", b);
    }
    let mut rules: Vec<&str> = data.lines().collect();
    while rules.len() > 0 {
//        println!("{}", rules.len());
        let mut next_rules: Vec<&str> = Vec::new();
        for line in rules.iter() {
            match line {
                // x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
                line if line.contains(" AND ") => {
                    let token: Vec<&str> = line.split(" ").collect();
                    let x = foo(&wires, token.get(0).unwrap());
                    let y = foo(&wires, token.get(2).unwrap());
                    let z = token.get(4).unwrap();
                    if x.is_err() || y.is_err() {
                        next_rules.push(line);
                    } else if !wires.contains_key(z) {
                        wires.insert(z, x.unwrap() & y.unwrap());
                    }
                }
                // x OR y -> z
                line if line.contains(" OR ") => {
                    let token: Vec<&str> = line.split(" ").collect();
                    let x = foo(&wires, token.get(0).unwrap());
                    let y = foo(&wires, token.get(2).unwrap());
                    let z = token.get(4).unwrap();
                    if x.is_err() || y.is_err() {
                        next_rules.push(line);
                    } else  if !wires.contains_key(z) {
                        wires.insert(z, x.unwrap() | y.unwrap());
                    }
                }
                // p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
                line if line.contains(" LSHIFT ") => {
                    let token: Vec<&str> = line.split(" ").collect();
                    let p = foo(&wires, token.get(0).unwrap());
                    let value = foo(&wires, token.get(2).unwrap());
                    let q = token.get(4).unwrap();
                    if p.is_err() || value.is_err() {
                        next_rules.push(line);
                    } else  if !wires.contains_key(q) {
                        wires.insert(q, p.unwrap() << value.unwrap());
                    }
                }
                // p RSHIFT 2 -> q
                line if line.contains(" RSHIFT ") => {
                    let token: Vec<&str> = line.split(" ").collect();
                    let p = foo(&wires, token.get(0).unwrap());
                    let value = foo(&wires, token.get(2).unwrap());
                    let q = token.get(4).unwrap();
                    if p.is_err() || value.is_err() {
                        next_rules.push(line);
                    } else  if !wires.contains_key(q) {
                        wires.insert(q, p.unwrap() >> value.unwrap());
                    }
                }
                // NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.
                line if line.contains("NOT ") => {
                    let token: Vec<&str> = line.split(" ").collect();
                    let e = foo(&wires, token.get(1).unwrap());
                    let f = token.get(3).unwrap();
                    if e.is_err() {
                        next_rules.push(line);
                    } else if !wires.contains_key(f)  {
                        wires.insert(f, !e.unwrap());
                    }
                }
                // 123 -> x means that the signal 123 is provided to wire x.
                _ => {
//                    println!("{line}");
                    let token: Vec<&str> = line.split(" ").collect();
                    let t0 = foo(&wires, token.get(0).unwrap());
                    let x = token.get(2).unwrap();
                    if t0.is_err() {
                        next_rules.push(line);
                    } else if !wires.contains_key(x) {
                        wires.insert(x, t0.unwrap());
                    }
                }
            }
        }
        rules = next_rules;
    }
    wires
}

pub fn part1(data: &str) -> u16 {
    part1_internal(data, 0)["a"]
}

pub fn part2(data: &str) -> u16 {
    let b = part1_internal(data, 0)["a"];
    part1_internal(data, b)["a"]
}

#[cfg(test)]
mod tests {
    use super::*;
    use std::collections::HashMap;

    #[test]
    fn tests_part1() {
        const INPUT: &str = "123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i";

        let actual = part1_internal(INPUT, 0);
        let expected = HashMap::from([
            ("d", 72),
            ("e", 507),
            ("f", 492),
            ("g", 114),
            ("h", 65412),
            ("i", 65079),
            ("x", 123),
            ("y", 456),
        ]);
        assert_eq!(actual, expected);
    }
}
