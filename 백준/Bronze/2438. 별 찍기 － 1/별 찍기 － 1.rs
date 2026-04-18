use std::io::{stdin, stdout, BufWriter, Write};

fn main() {
    let mut ob = BufWriter::new(stdout());

    let mut s = String::new();
    stdin().read_line(&mut s).unwrap();
    let s: i32 = s.trim().parse().unwrap();
    for i in 1..s+1 {
        for _ in 0..i{
            write!(ob, "*").unwrap();
        }
        writeln!(ob).unwrap();
    }
}
