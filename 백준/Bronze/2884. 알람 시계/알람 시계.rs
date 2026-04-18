use std::io::stdin;

fn main() {
    let mut a = String::new();
    stdin()
        .read_line(&mut a)
        .unwrap();
    let a: Vec<&str> = a
        .trim()
        .split_whitespace()
        .collect();
    let mut hour = a[0].parse::<i8>().unwrap();
    let mut minute = a[1].parse::<i8>().unwrap() - 45;
    if minute < 0{
        hour -= 1;
        minute += 60;
    }
    if hour < 0{
        hour += 24;
    }
    println!("{} {}", hour, minute);
}
