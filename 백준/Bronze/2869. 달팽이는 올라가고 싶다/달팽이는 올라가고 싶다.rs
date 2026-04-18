use std::io;

fn main() {
    let mut buf = String::new();
    io::stdin().read_line(&mut buf).unwrap();
    let buf: Vec<_> = buf.split_whitespace().map(|x| x.parse::<f64>().unwrap()).collect();
    let a = (buf[2] - buf[1]) / (buf[0] - buf[1]);
    println!("{}",  if a % 1. == 0. {a} else {a + (-(a % 1.)) + 1.})
}
