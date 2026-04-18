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
    let a = s.parse::<i32>().unwrap();
    if ((a % 4 == 0) && a % 100 != 0) || a % 400 == 0{
        println!("1")
    }else{
        println!("0")
    }
}
