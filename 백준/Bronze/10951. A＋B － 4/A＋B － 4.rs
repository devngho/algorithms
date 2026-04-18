use std::io;
use io::Write;
use io::BufRead;

fn main() {
    let stdout = io::stdout();
    let mut out = io::BufWriter::new(stdout.lock());
    let stdin = io::stdin();
    let mut inp = io::BufReader::new(stdin.lock());
    loop{
        let mut x = String::new();
        let bytes = inp.read_line(&mut x).unwrap();
        if bytes == 0{
            break
        }
        let inp: Vec<i32> = x.split_whitespace().map(|b| b.parse::<i32>().unwrap()).collect();
        writeln!(out, "{}", inp[0] + inp[1]).unwrap();
    }
}