use std::io::stdin;

fn main() {
    let mut a = String::new();
    stdin()
        .read_line(&mut a)
        .unwrap();
    let a: i8 = a
        .trim()
        .parse()
        .unwrap();
    for i in 1..10{
        println!("{} * {} = {}", a, i, a * i)
    }
}
