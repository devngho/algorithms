use std::io::{self, Write, BufRead};

fn main() {
    let stdout = io::stdout();
    let mut out = io::BufWriter::new(stdout.lock());
    let stdin = io::stdin();
    let mut inp = io::BufReader::new(stdin.lock());
    let mut buf = String::new();
    inp.read_line(&mut buf).unwrap();
    for _ in 0..buf.trim_end().parse::<i32>().unwrap(){
        buf.clear();
        inp.read_line(&mut buf).unwrap();
        let s = buf.trim_end().split_whitespace().map(|x| x.parse::<i32>().unwrap()).collect::<Vec<i32>>();
        let avg = &s[1..].iter().sum() / s[0];
        writeln!(out, "{:.3}%", *(&s[1..].iter().filter(|x| **x > avg).count()) as f64 / s[0] as f64 * 100.);
    }
}