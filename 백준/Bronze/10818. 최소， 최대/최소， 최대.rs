use std::io::stdin;

fn main() {
    stdin()
        .read_line(&mut String::new())
        .expect("Did not enter a correct string");
    let mut a = String::new();
    stdin()
        .read_line(&mut a)
        .expect("Did not enter a correct string");
    if let Some('\n') = a.chars().next_back() {
        a.pop();
    }
    if let Some('\r') = a.chars().next_back() {
        a.pop();
    }
    let a = a.split(" ").map(|x| x.parse::<i32>().unwrap()).collect::<Vec<i32>>();
    println!("{} {}", a.iter().min().unwrap(), a.iter().max().unwrap())
}
