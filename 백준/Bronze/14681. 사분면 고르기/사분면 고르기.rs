use std::io::{stdin,stdout,Write};

fn main() {
    let mut a=String::new();
    let mut b = String::new();
    let _ = stdout().flush();
    stdin().read_line(&mut a).expect("Did not enter a correct string");
    if let Some('\n')=a.chars().next_back() {
        a.pop();
    }
    if let Some('\r')=a.chars().next_back() {
        a.pop();
    }
    stdin().read_line(&mut b).expect("Did not enter a correct string");
    if let Some('\n')=b.chars().next_back() {
        b.pop();
    }
    if let Some('\r')=b.chars().next_back() {
        b.pop();
    }
    let a = a.parse::<i32>().unwrap();
    let b = b.parse::<i32>().unwrap();
    if a > 0{
        if b > 0{
            println!("1");
        }else{
            println!("4");
        }
    }else{
        if b > 0{
            println!("2");
        }else{
            println!("3");
        }
    }
}
