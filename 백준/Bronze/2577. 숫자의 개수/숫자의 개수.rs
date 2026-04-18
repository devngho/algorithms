use std::{io, char};

fn main() {
    let mut sum = String::new();
    {
        let mut a = String::new();
        io::stdin().read_line(&mut a).unwrap();
        let a: i32 = a.trim().parse().unwrap();
        let mut b = String::new();
        io::stdin().read_line(&mut b).unwrap();
        let b: i32 = b.trim().parse().unwrap();
        let mut c = String::new();
        io::stdin().read_line(&mut c).unwrap();
        let c: i32 = c.trim().parse().unwrap();
        sum = (a * b * c).to_string();
    }
    for i in 0..10{
        println!("{}", sum.chars().filter(|x| *x == char::from_digit(i, 10).unwrap()).count())
    }
}
