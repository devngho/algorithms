use std::io;

fn main() {
    let mut buf = String::new();
    io::stdin().read_line(&mut buf).unwrap();
    buf.clear();
    io::stdin().read_line(&mut buf).unwrap();
    println!("{}", buf.trim().chars().map(|x| x.to_digit(10).unwrap()).sum::<u32>());
}