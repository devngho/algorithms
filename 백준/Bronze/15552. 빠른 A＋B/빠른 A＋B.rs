use std::io;
use io::Write;
use io::BufRead;

fn main() {
    let stdout = io::stdout();
    let mut out = io::BufWriter::new(stdout.lock());
    let stdin = io::stdin();
    let mut inp = io::BufReader::new(stdin.lock());
    let mut t = String::new();
    inp.read_line(&mut t)
        .unwrap();
    for _ in 0..t.trim().parse().unwrap(){
        let mut x = String::new();
        inp.read_line(&mut x)
            .unwrap();
        writeln!(out, "{}", x.split_whitespace().map(|b| b.parse::<i32>().unwrap()).sum::<i32>()).unwrap();
    }
}