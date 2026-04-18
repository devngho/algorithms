use std::io::{self, Write, BufRead};

fn main() {
    let mut buf = String::new();
    let mut out = io::BufWriter::new(io::stdout());
    let mut inp = io::BufReader::new(io::stdin());
    inp.read_line(&mut buf).unwrap();
    for _ in 0..buf.trim_end().parse::<i32>().unwrap(){
        buf.clear();
        inp.read_line(&mut buf).unwrap();
        let mut buf = buf.split_whitespace();
        let c = buf.next().unwrap().parse::<i32>().unwrap() as usize;
        for r in buf.next().unwrap().chars(){
            write!(out, "{}", String::from(r).repeat(c)).unwrap();
        }
        writeln!(out).unwrap();
    }
}