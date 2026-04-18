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
    for i in 0..t.trim().parse().unwrap(){
        let mut x = String::new();
        inp.read_line(&mut x)
            .unwrap();
        let inp: Vec<i32> = x.split_whitespace().map(|b| b.parse::<i32>().unwrap()).collect();
        writeln!(out, "Case #{}: {} + {} = {}", i+1, inp[0], inp[1], inp[0] + inp[1]).unwrap();
    }
}