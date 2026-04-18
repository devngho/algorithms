use std::io::{self, Read};

fn main() {
    let mut s = String::new();
    io::stdin().read_to_string(&mut s).unwrap();
    let (x, y) = s.lines()
        .map(|x| x.parse::<i32>().unwrap())
        .enumerate()
        .max_by_key(|&(_,y)| y)
        .unwrap();
    println!("{}\n{}", y, x + 1);
}