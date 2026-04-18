use std::cmp::Ordering;
use std::io::{stdin,stdout,Write};

fn main() {
    let mut s=String::new();
    let _=stdout().flush();
    stdin().read_line(&mut s).expect("Did not enter a correct string");
    if let Some('\n')=s.chars().next_back() {
        s.pop();
    }
    if let Some('\r')=s.chars().next_back() {
        s.pop();
    }
    let s = s.split(" ");
    let s = s.collect::<Vec<&str>>();
    let a = s[0].parse::<i32>().unwrap();
    let b = s[1].parse::<i32>().unwrap();
    match a.cmp(&b) {
        Ordering::Less => println!("<"),
        Ordering::Equal => println!("=="),
        Ordering::Greater => println!(">")
    }
}
