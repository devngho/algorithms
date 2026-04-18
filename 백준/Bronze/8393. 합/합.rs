use std::io::stdin;

fn main() {
    let mut a = String::new();
    stdin()
        .read_line(&mut a)
        .unwrap();
    let a: i32 = a
        .trim()
        .parse()
        .unwrap();
    let mut res = 0;
    for i in 1..a+1{
        res += i;
    }
    println!("{}", res)
}
