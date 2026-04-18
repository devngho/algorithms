use std::io;

fn main() {
    let mut buf = String::new();
    io::stdin().read_line(&mut buf).unwrap();
    println!("{}", buf.trim().chars().collect::<Vec<char>>()[0] as u8);
}