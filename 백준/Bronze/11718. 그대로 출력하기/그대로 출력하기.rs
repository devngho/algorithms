use std::io::{self, Write};

fn main() {
    let mut buf = String::new();
    let mut out = io::BufWriter::new(io::stdout());
    loop{
        if io::stdin().read_line(&mut buf).unwrap() == 0{
            break
        }
        writeln!(out, "{}", buf.trim());
        buf.clear()
    }
}
